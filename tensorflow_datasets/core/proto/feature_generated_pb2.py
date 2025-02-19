# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='feature.proto',
    package='tensorflow_datasets',
    syntax='proto3',
    serialized_options=b'\370\001\001',
    serialized_pb=b'\n\rfeature.proto\x12\x13tensorflow_datasets\"\xa0\x01\n\x0c\x46\x65\x61turesDict\x12\x41\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32/.tensorflow_datasets.FeaturesDict.FeaturesEntry\x1aM\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.tensorflow_datasets.Feature:\x02\x38\x01\"i\n\x07\x46\x65\x61ture\x12\x19\n\x11python_class_name\x18\x01 \x01(\t\x12\x38\n\x0cjson_feature\x18\x02 \x01(\x0b\x32 .tensorflow_datasets.JsonFeatureH\x00\x42\t\n\x07\x63ontent\"\x1b\n\x0bJsonFeature\x12\x0c\n\x04json\x18\x01 \x01(\tB\x03\xf8\x01\x01\x62\x06proto3'
)

_FEATURESDICT_FEATURESENTRY = _descriptor.Descriptor(
    name='FeaturesEntry',
    full_name='tensorflow_datasets.FeaturesDict.FeaturesEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='tensorflow_datasets.FeaturesDict.FeaturesEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='tensorflow_datasets.FeaturesDict.FeaturesEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=122,
    serialized_end=199,
)

_FEATURESDICT = _descriptor.Descriptor(
    name='FeaturesDict',
    full_name='tensorflow_datasets.FeaturesDict',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='features',
            full_name='tensorflow_datasets.FeaturesDict.features',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[
        _FEATURESDICT_FEATURESENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=39,
    serialized_end=199,
)

_FEATURE = _descriptor.Descriptor(
    name='Feature',
    full_name='tensorflow_datasets.Feature',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='python_class_name',
            full_name='tensorflow_datasets.Feature.python_class_name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='json_feature',
            full_name='tensorflow_datasets.Feature.json_feature',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='content',
            full_name='tensorflow_datasets.Feature.content',
            index=0,
            containing_type=None,
            fields=[]),
    ],
    serialized_start=201,
    serialized_end=306,
)

_JSONFEATURE = _descriptor.Descriptor(
    name='JsonFeature',
    full_name='tensorflow_datasets.JsonFeature',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='json',
            full_name='tensorflow_datasets.JsonFeature.json',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b''.decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=308,
    serialized_end=335,
)

_FEATURESDICT_FEATURESENTRY.fields_by_name['value'].message_type = _FEATURE
_FEATURESDICT_FEATURESENTRY.containing_type = _FEATURESDICT
_FEATURESDICT.fields_by_name[
    'features'].message_type = _FEATURESDICT_FEATURESENTRY
_FEATURE.fields_by_name['json_feature'].message_type = _JSONFEATURE
_FEATURE.oneofs_by_name['content'].fields.append(
    _FEATURE.fields_by_name['json_feature'])
_FEATURE.fields_by_name[
    'json_feature'].containing_oneof = _FEATURE.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['FeaturesDict'] = _FEATURESDICT
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['JsonFeature'] = _JSONFEATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeaturesDict = _reflection.GeneratedProtocolMessageType(
    'FeaturesDict',
    (_message.Message,),
    {
        'FeaturesEntry':
            _reflection.GeneratedProtocolMessageType(
                'FeaturesEntry',
                (_message.Message,),
                {
                    'DESCRIPTOR': _FEATURESDICT_FEATURESENTRY,
                    '__module__': 'feature_pb2'
                    # @@protoc_insertion_point(class_scope:tensorflow_datasets.FeaturesDict.FeaturesEntry)
                }),
        'DESCRIPTOR':
            _FEATURESDICT,
        '__module__':
            'feature_pb2'
        # @@protoc_insertion_point(class_scope:tensorflow_datasets.FeaturesDict)
    })
_sym_db.RegisterMessage(FeaturesDict)
_sym_db.RegisterMessage(FeaturesDict.FeaturesEntry)

Feature = _reflection.GeneratedProtocolMessageType(
    'Feature',
    (_message.Message,),
    {
        'DESCRIPTOR': _FEATURE,
        '__module__': 'feature_pb2'
        # @@protoc_insertion_point(class_scope:tensorflow_datasets.Feature)
    })
_sym_db.RegisterMessage(Feature)

JsonFeature = _reflection.GeneratedProtocolMessageType(
    'JsonFeature',
    (_message.Message,),
    {
        'DESCRIPTOR': _JSONFEATURE,
        '__module__': 'feature_pb2'
        # @@protoc_insertion_point(class_scope:tensorflow_datasets.JsonFeature)
    })
_sym_db.RegisterMessage(JsonFeature)

DESCRIPTOR._options = None
_FEATURESDICT_FEATURESENTRY._options = None
# @@protoc_insertion_point(module_scope)
