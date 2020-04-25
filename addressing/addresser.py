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

import enum
import hashlib
from io import BytesIO

FAMILY_NAME = 'docs_blocks'
FAMILY_VERSION = '0.1'
NAMESPACE = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[:6]
AGENT_PREFIX = '00'
RECORD_PREFIX = '01'
DOCUMENT_PREFIX = '02'


@enum.unique
class AddressSpace(enum.IntEnum):
    AGENT = 0
    RECORD = 1
    DOCUMENT = 2
    OTHER_FAMILY = 100


def get_agent_address(public_key):
    return NAMESPACE + AGENT_PREFIX + hashlib.sha512(
        public_key.encode('utf-8')).hexdigest()[:62]


def get_record_address(record_id):
    return NAMESPACE + RECORD_PREFIX + hashlib.sha512(
        record_id.encode('utf-8')).hexdigest()[:62]


def get_address_type(address):
    if address[:len(NAMESPACE)] != NAMESPACE:
        return AddressSpace.OTHER_FAMILY

    infix = address[6:8]
    """ Pega o segundo bloco do endereço
    """
    if infix == '00':
        return AddressSpace.AGENT
    if infix == '01':
        return AddressSpace.RECORD
    if infix == '02':
        return AddressSpace.DOCUMENT

    return AddressSpace.OTHER_FAMILY

def get_document_address(document):
    # separar em blocos para não ocupar memória 
    # inteira com arquivos grandes
    BLOCK_SIZE = 65536*2
    file_hash = hashlib.sha512()
    
    with BytesIO(document) as f:
        fb = f.read(BLOCK_SIZE)

        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    
    return NAMESPACE + DOCUMENT_PREFIX + file_hash.hexdigest()[:62]