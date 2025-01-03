# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki_vector/messaging/response_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='anki_vector/messaging/response_status.proto',
  package='Anki.Vector.external_interface',
  syntax='proto3',
  serialized_pb=_b('\n+anki_vector/messaging/response_status.proto\x12\x1e\x41nki.Vector.external_interface\"\xe8\x01\n\x0eResponseStatus\x12G\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x39.Anki.Vector.external_interface.ResponseStatus.StatusCode\"\x8c\x01\n\nStatusCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x15\n\x11RESPONSE_RECEIVED\x10\x01\x12\x16\n\x12REQUEST_PROCESSING\x10\x02\x12\x06\n\x02OK\x10\x03\x12\r\n\tFORBIDDEN\x10\x64\x12\r\n\tNOT_FOUND\x10\x65\x12\x1c\n\x18\x45RROR_UPDATE_IN_PROGRESS\x10\x66\x62\x06proto3')
)



_RESPONSESTATUS_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='Anki.Vector.external_interface.ResponseStatus.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_RECEIVED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_PROCESSING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=4, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=5, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UPDATE_IN_PROGRESS', index=6, number=102,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=312,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS_STATUSCODE)


_RESPONSESTATUS = _descriptor.Descriptor(
  name='ResponseStatus',
  full_name='Anki.Vector.external_interface.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Anki.Vector.external_interface.ResponseStatus.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSESTATUS_STATUSCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=312,
)

_RESPONSESTATUS.fields_by_name['code'].enum_type = _RESPONSESTATUS_STATUSCODE
_RESPONSESTATUS_STATUSCODE.containing_type = _RESPONSESTATUS
DESCRIPTOR.message_types_by_name['ResponseStatus'] = _RESPONSESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseStatus = _reflection.GeneratedProtocolMessageType('ResponseStatus', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESTATUS,
  __module__ = 'anki_vector.messaging.response_status_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ResponseStatus)
  ))
_sym_db.RegisterMessage(ResponseStatus)


# @@protoc_insertion_point(module_scope)
