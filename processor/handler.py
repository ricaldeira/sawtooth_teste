# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import datetime
import time
import logging
from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction

from addressing import addresser

from protobufs.protos import payload_pb2
from protobufs.protos import car_payload_pb2
from processor.payload import SimpleSupplyPayload
from processor.car_processor.payload import CarTrackerPayload
from processor.state import SimpleSupplyState

SYNC_TOLERANCE = 60 * 5
MAX_LAT = 90 * 1e6
MIN_LAT = -90 * 1e6
MAX_LNG = 180 * 1e6
MIN_LNG = -180 * 1e6

LOGGER = logging.getLogger(__name__)

class SimpleSupplyHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespaces(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = SimpleSupplyPayload(transaction.payload)
        state = SimpleSupplyState(context)
        try: 
            _validate_timestamp(payload.timestamp)

            if payload.action == payload_pb2.SimpleSupplyPayload.CREATE_AGENT:
                _create_agent(
                    state=state,
                    public_key=header.signer_public_key,
                    payload=payload)
            elif payload.action == payload_pb2.SimpleSupplyPayload.CREATE_RECORD:
                _create_record(
                    state=state,
                    public_key=header.signer_public_key,
                    payload=payload)
            elif payload.action == payload_pb2.SimpleSupplyPayload.TRANSFER_RECORD:
                _transfer_record(
                    state=state,
                    public_key=header.signer_public_key,
                    payload=payload)
            elif payload.action == payload_pb2.SimpleSupplyPayload.UPDATE_RECORD:
                _update_record(
                    state=state,
                    public_key=header.signer_public_key,
                    payload=payload)
            elif payload.action == payload_pb2.SimpleSupplyPayload.CREATE_DOCUMENT:
                _create_document(
                    state=state,
                    signer_public_key=header.signer_public_key,
                    payload=payload)
            
            elif payload.action == car_payload_pb2.CarTrackerPayload.CREATE_CAR:
                LOGGER.info('[PROCESSOR HANDLER] Receiving payload of type CREATE_CAR')
                _create_car(
                    state=state,
                    signer_public_key=header.signer_public_key,
                    payload=payload)


            else:
                raise InvalidTransaction('Unhandled action')
        except:
            LOGGER.error("Erro no processamento SimplySupplyHandler . change the name of it") 
            print("Erro no processamento!!!")

def _create_agent(state, public_key, payload):
    if state.get_agent(public_key):
        raise InvalidTransaction('Agent with the public key {} already '
                                 'exists'.format(public_key))
    state.set_agent(
        public_key=public_key,
        name=payload.data.name,
        timestamp=payload.timestamp)


def _create_record(state, public_key, payload):
    if state.get_agent(public_key) is None:
        raise InvalidTransaction('Agent with the public key {} does '
                                 'not exist'.format(public_key))

    if payload.data.record_id == '':
        raise InvalidTransaction('No record ID provided')

    if state.get_record(payload.data.record_id):
        raise InvalidTransaction('Identifier {} belongs to an existing '
                                 'record'.format(payload.data.record_id))

    _validate_latlng(payload.data.latitude, payload.data.longitude)

    state.set_record(
        public_key=public_key,
        latitude=payload.data.latitude,
        longitude=payload.data.longitude,
        record_id=payload.data.record_id,
        timestamp=payload.timestamp)


def _transfer_record(state, public_key, payload):
    if state.get_agent(payload.data.receiving_agent) is None:
        raise InvalidTransaction(
            'Agent with the public key {} does '
            'not exist'.format(payload.data.receiving_agent))

    record = state.get_record(payload.data.record_id)
    if record is None:
        raise InvalidTransaction('Record with the record id {} does not '
                                 'exist'.format(payload.data.record_id))

    if not _validate_record_owner(signer_public_key=public_key,
                                  record=record):
        raise InvalidTransaction(
            'Transaction signer is not the owner of the record')

    state.transfer_record(
        receiving_agent=payload.data.receiving_agent,
        record_id=payload.data.record_id,
        timestamp=payload.timestamp)


def _update_record(state, public_key, payload):
    record = state.get_record(payload.data.record_id)
    if record is None:
        raise InvalidTransaction('Record with the record id {} does not '
                                 'exist'.format(payload.data.record_id))

    if not _validate_record_owner(signer_public_key=public_key,
                                  record=record):
        raise InvalidTransaction(
            'Transaction signer is not the owner of the record')

    _validate_latlng(payload.data.latitude, payload.data.longitude)

    state.update_record(
        latitude=payload.data.latitude,
        longitude=payload.data.longitude,
        record_id=payload.data.record_id,
        timestamp=payload.timestamp)


def _validate_record_owner(signer_public_key, record):
    """Validates that the public key of the signer is the latest (i.e.
    current) owner of the record
    """
    latest_owner = max(record.owners, key=lambda obj: obj.timestamp).agent_id
    return latest_owner == signer_public_key


def _validate_latlng(latitude, longitude):
    if not MIN_LAT <= latitude <= MAX_LAT:
        raise InvalidTransaction('Latitude must be between -90 and 90. '
                                 'Got {}'.format(latitude/1e6))
    if not MIN_LNG <= longitude <= MAX_LNG:
        raise InvalidTransaction('Longitude must be between -180 and 180. '
                                 'Got {}'.format(longitude/1e6))


def _validate_timestamp(timestamp):
    """Validates that the client submitted timestamp for a transaction is not
    greater than current time, within a tolerance defined by SYNC_TOLERANCE

    NOTE: Timestamp validation can be challenging since the machines that are
    submitting and validating transactions may have different system times
    """
    dts = datetime.datetime.utcnow()
    current_time = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
    if (timestamp - current_time) > SYNC_TOLERANCE:
        raise InvalidTransaction(
            'Timestamp must be less than local time.'
            ' Expected {0} in ({1}-{2}, {1}+{2})'.format(
                timestamp, current_time, SYNC_TOLERANCE))

def _create_document(state, signer_public_key, payload):
    if state.get_agent(signer_public_key) is None:
        raise InvalidTransaction('Agent with the public key {} does '
                                 'not exist'.format(signer_public_key))
    if payload.data.document_hash  is None:
        raise InvalidTransaction('Hash do documento invalido ou vazio')
    state.set_document(
                    public_key=signer_public_key,
                    document_hash=payload.data.document_hash,
                    file_name=payload.data.file_name,                    
                    timestamp=payload.timestamp)

def _create_car(state, signer_public_key, payload):
    LOGGER.debug('[PROCESSOR HANDLER] @_create_car with paylod' + payload.data)    
    if state.get_agent(signer_public_key) is None:
        LOGGER.error('[PROCESSOR HANDLER] @_create_car:: Invalid agent')
        raise InvalidTransaction('Agent with the public key {} does '
                                 'not exist'.format(signer_public_key))
    if payload.data.chassis is None:
        LOGGER.error('[PROCESSOR HANDLER] @_create_car:: Invalid car chassis')
        raise InvalidTransaction('Invalid chassis')

    state.set_car(public_key=signer_public_key,
                timestamp=payload.timestamp,
                chassis=payload.data.chassi, 
                license=payload.data.license, 
                yearManufactured=payload.data.yearManufactured, 
                yearModel=payload.data.yearModel,
                color=payload.data.color, 
                brand=payload.data.brand, 
                model=payload.data.model)