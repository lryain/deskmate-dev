# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki_vector/messaging/behavior.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki_vector.messaging import messages_pb2 as anki__vector_dot_messaging_dot_messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='anki_vector/messaging/behavior.proto',
  package='Anki.Vector.external_interface',
  syntax='proto3',
  serialized_pb=_b('\n$anki_vector/messaging/behavior.proto\x12\x1e\x41nki.Vector.external_interface\x1a$anki_vector/messaging/messages.proto\"\x10\n\x0e\x43ontrolRelease\"\xae\x01\n\x0e\x43ontrolRequest\x12I\n\x08priority\x18\x01 \x01(\x0e\x32\x37.Anki.Vector.external_interface.ControlRequest.Priority\"Q\n\x08Priority\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12OVERRIDE_BEHAVIORS\x10\n\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x14\x12\x13\n\x0fRESERVE_CONTROL\x10\x1e\"\xbe\x01\n\x16\x42\x65haviorControlRequest\x12I\n\x0f\x63ontrol_release\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ControlReleaseH\x00\x12I\n\x0f\x63ontrol_request\x18\x02 \x01(\x0b\x32..Anki.Vector.external_interface.ControlRequestH\x00\x42\x0e\n\x0crequest_type\"\x18\n\x16\x43ontrolGrantedResponse\"\x15\n\x13\x43ontrolLostResponse\"\x1d\n\x1bReservedControlLostResponse\"\x82\x03\n\x17\x42\x65haviorControlResponse\x12Z\n\x18\x63ontrol_granted_response\x18\x01 \x01(\x0b\x32\x36.Anki.Vector.external_interface.ControlGrantedResponseH\x00\x12Q\n\x12\x63ontrol_lost_event\x18\x02 \x01(\x0b\x32\x33.Anki.Vector.external_interface.ControlLostResponseH\x00\x12\x43\n\nkeep_alive\x18\x03 \x01(\x0b\x32-.Anki.Vector.external_interface.KeepAlivePingH\x00\x12\x62\n\x1breserved_control_lost_event\x18\x04 \x01(\x0b\x32;.Anki.Vector.external_interface.ReservedControlLostResponseH\x00\x42\x0f\n\rresponse_typeb\x06proto3')
  ,
  dependencies=[anki__vector_dot_messaging_dot_messages__pb2.DESCRIPTOR,])



_CONTROLREQUEST_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='Anki.Vector.external_interface.ControlRequest.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERRIDE_BEHAVIORS', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=2, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESERVE_CONTROL', index=3, number=30,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=222,
  serialized_end=303,
)
_sym_db.RegisterEnumDescriptor(_CONTROLREQUEST_PRIORITY)


_CONTROLRELEASE = _descriptor.Descriptor(
  name='ControlRelease',
  full_name='Anki.Vector.external_interface.ControlRelease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=126,
)


_CONTROLREQUEST = _descriptor.Descriptor(
  name='ControlRequest',
  full_name='Anki.Vector.external_interface.ControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='Anki.Vector.external_interface.ControlRequest.priority', index=0,
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
    _CONTROLREQUEST_PRIORITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=303,
)


_BEHAVIORCONTROLREQUEST = _descriptor.Descriptor(
  name='BehaviorControlRequest',
  full_name='Anki.Vector.external_interface.BehaviorControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control_release', full_name='Anki.Vector.external_interface.BehaviorControlRequest.control_release', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_request', full_name='Anki.Vector.external_interface.BehaviorControlRequest.control_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request_type', full_name='Anki.Vector.external_interface.BehaviorControlRequest.request_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=306,
  serialized_end=496,
)


_CONTROLGRANTEDRESPONSE = _descriptor.Descriptor(
  name='ControlGrantedResponse',
  full_name='Anki.Vector.external_interface.ControlGrantedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=522,
)


_CONTROLLOSTRESPONSE = _descriptor.Descriptor(
  name='ControlLostResponse',
  full_name='Anki.Vector.external_interface.ControlLostResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=545,
)


_RESERVEDCONTROLLOSTRESPONSE = _descriptor.Descriptor(
  name='ReservedControlLostResponse',
  full_name='Anki.Vector.external_interface.ReservedControlLostResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=576,
)


_BEHAVIORCONTROLRESPONSE = _descriptor.Descriptor(
  name='BehaviorControlResponse',
  full_name='Anki.Vector.external_interface.BehaviorControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control_granted_response', full_name='Anki.Vector.external_interface.BehaviorControlResponse.control_granted_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_lost_event', full_name='Anki.Vector.external_interface.BehaviorControlResponse.control_lost_event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_alive', full_name='Anki.Vector.external_interface.BehaviorControlResponse.keep_alive', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved_control_lost_event', full_name='Anki.Vector.external_interface.BehaviorControlResponse.reserved_control_lost_event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response_type', full_name='Anki.Vector.external_interface.BehaviorControlResponse.response_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=579,
  serialized_end=965,
)

_CONTROLREQUEST.fields_by_name['priority'].enum_type = _CONTROLREQUEST_PRIORITY
_CONTROLREQUEST_PRIORITY.containing_type = _CONTROLREQUEST
_BEHAVIORCONTROLREQUEST.fields_by_name['control_release'].message_type = _CONTROLRELEASE
_BEHAVIORCONTROLREQUEST.fields_by_name['control_request'].message_type = _CONTROLREQUEST
_BEHAVIORCONTROLREQUEST.oneofs_by_name['request_type'].fields.append(
  _BEHAVIORCONTROLREQUEST.fields_by_name['control_release'])
_BEHAVIORCONTROLREQUEST.fields_by_name['control_release'].containing_oneof = _BEHAVIORCONTROLREQUEST.oneofs_by_name['request_type']
_BEHAVIORCONTROLREQUEST.oneofs_by_name['request_type'].fields.append(
  _BEHAVIORCONTROLREQUEST.fields_by_name['control_request'])
_BEHAVIORCONTROLREQUEST.fields_by_name['control_request'].containing_oneof = _BEHAVIORCONTROLREQUEST.oneofs_by_name['request_type']
_BEHAVIORCONTROLRESPONSE.fields_by_name['control_granted_response'].message_type = _CONTROLGRANTEDRESPONSE
_BEHAVIORCONTROLRESPONSE.fields_by_name['control_lost_event'].message_type = _CONTROLLOSTRESPONSE
_BEHAVIORCONTROLRESPONSE.fields_by_name['keep_alive'].message_type = anki__vector_dot_messaging_dot_messages__pb2._KEEPALIVEPING
_BEHAVIORCONTROLRESPONSE.fields_by_name['reserved_control_lost_event'].message_type = _RESERVEDCONTROLLOSTRESPONSE
_BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type'].fields.append(
  _BEHAVIORCONTROLRESPONSE.fields_by_name['control_granted_response'])
_BEHAVIORCONTROLRESPONSE.fields_by_name['control_granted_response'].containing_oneof = _BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type']
_BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type'].fields.append(
  _BEHAVIORCONTROLRESPONSE.fields_by_name['control_lost_event'])
_BEHAVIORCONTROLRESPONSE.fields_by_name['control_lost_event'].containing_oneof = _BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type']
_BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type'].fields.append(
  _BEHAVIORCONTROLRESPONSE.fields_by_name['keep_alive'])
_BEHAVIORCONTROLRESPONSE.fields_by_name['keep_alive'].containing_oneof = _BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type']
_BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type'].fields.append(
  _BEHAVIORCONTROLRESPONSE.fields_by_name['reserved_control_lost_event'])
_BEHAVIORCONTROLRESPONSE.fields_by_name['reserved_control_lost_event'].containing_oneof = _BEHAVIORCONTROLRESPONSE.oneofs_by_name['response_type']
DESCRIPTOR.message_types_by_name['ControlRelease'] = _CONTROLRELEASE
DESCRIPTOR.message_types_by_name['ControlRequest'] = _CONTROLREQUEST
DESCRIPTOR.message_types_by_name['BehaviorControlRequest'] = _BEHAVIORCONTROLREQUEST
DESCRIPTOR.message_types_by_name['ControlGrantedResponse'] = _CONTROLGRANTEDRESPONSE
DESCRIPTOR.message_types_by_name['ControlLostResponse'] = _CONTROLLOSTRESPONSE
DESCRIPTOR.message_types_by_name['ReservedControlLostResponse'] = _RESERVEDCONTROLLOSTRESPONSE
DESCRIPTOR.message_types_by_name['BehaviorControlResponse'] = _BEHAVIORCONTROLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlRelease = _reflection.GeneratedProtocolMessageType('ControlRelease', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLRELEASE,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ControlRelease)
  ))
_sym_db.RegisterMessage(ControlRelease)

ControlRequest = _reflection.GeneratedProtocolMessageType('ControlRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLREQUEST,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ControlRequest)
  ))
_sym_db.RegisterMessage(ControlRequest)

BehaviorControlRequest = _reflection.GeneratedProtocolMessageType('BehaviorControlRequest', (_message.Message,), dict(
  DESCRIPTOR = _BEHAVIORCONTROLREQUEST,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.BehaviorControlRequest)
  ))
_sym_db.RegisterMessage(BehaviorControlRequest)

ControlGrantedResponse = _reflection.GeneratedProtocolMessageType('ControlGrantedResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLGRANTEDRESPONSE,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ControlGrantedResponse)
  ))
_sym_db.RegisterMessage(ControlGrantedResponse)

ControlLostResponse = _reflection.GeneratedProtocolMessageType('ControlLostResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLOSTRESPONSE,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ControlLostResponse)
  ))
_sym_db.RegisterMessage(ControlLostResponse)

ReservedControlLostResponse = _reflection.GeneratedProtocolMessageType('ReservedControlLostResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESERVEDCONTROLLOSTRESPONSE,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ReservedControlLostResponse)
  ))
_sym_db.RegisterMessage(ReservedControlLostResponse)

BehaviorControlResponse = _reflection.GeneratedProtocolMessageType('BehaviorControlResponse', (_message.Message,), dict(
  DESCRIPTOR = _BEHAVIORCONTROLRESPONSE,
  __module__ = 'anki_vector.messaging.behavior_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.BehaviorControlResponse)
  ))
_sym_db.RegisterMessage(BehaviorControlResponse)


# @@protoc_insertion_point(module_scope)