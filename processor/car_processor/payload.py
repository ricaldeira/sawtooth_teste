from sawtooth_sdk.processor.exceptions import InvalidTransaction

from protobufs.protos import car_payload_pb2
import logging

LOGGER = logging.getLogger(__name__)

class CarTrackerPayload(object):
    def __init__(self, payload):
        self._transaction = car_payload_pb2.CarTrackerPayload()
        self._transaction.ParseFromString(payload)
    
    @property
    def action(self):
        return self._transaction.action
    
    @property
    def data(self):
        if self._transaction.HasField('create_car') and \
            self._transaction.action == \
                car_payload_pb2.CarTrackerPayload.CREATE_CAR:
                LOGGER.info("[Payload] Receiving CREATE_CAR message")
                return self._transaction.create_car
        if self._transaction.HasField('update_car') and \
            self._transaction.action == \
                car_payload_pb2.CarTrackerPayload.UPDAATE_CAR:
                LOGGER.info("[Payload] Receiving UPDATE_CAR message")
                return self._transaction.update_car
        
        LOGGER.error('Action does not match CAR TRACKER data')
        raise InvalidTransaction('Action does not match CAR TRACKER data')
    
    @property
    def timestamp(self):
        return self._transaction.timestamp