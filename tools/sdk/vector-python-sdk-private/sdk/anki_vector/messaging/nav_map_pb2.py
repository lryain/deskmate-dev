# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki_vector/messaging/nav_map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='anki_vector/messaging/nav_map.proto',
  package='Anki.Vector.external_interface',
  syntax='proto3',
  serialized_pb=_b('\n#anki_vector/messaging/nav_map.proto\x12\x1e\x41nki.Vector.external_interface\"x\n\x0eNavMapQuadInfo\x12\x43\n\x07\x63ontent\x18\x01 \x01(\x0e\x32\x32.Anki.Vector.external_interface.NavNodeContentType\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\r\x12\x12\n\ncolor_rgba\x18\x03 \x01(\r\"{\n\nNavMapInfo\x12\x12\n\nroot_depth\x18\x01 \x01(\x05\x12\x14\n\x0croot_size_mm\x18\x02 \x01(\x02\x12\x15\n\rroot_center_x\x18\x03 \x01(\x02\x12\x15\n\rroot_center_y\x18\x04 \x01(\x02\x12\x15\n\rroot_center_z\x18\x05 \x01(\x02\"&\n\x11NavMapFeedRequest\x12\x11\n\tfrequency\x18\x01 \x01(\x02\"\xa9\x01\n\x12NavMapFeedResponse\x12\x11\n\torigin_id\x18\x01 \x01(\r\x12<\n\x08map_info\x18\x02 \x01(\x0b\x32*.Anki.Vector.external_interface.NavMapInfo\x12\x42\n\nquad_infos\x18\x03 \x03(\x0b\x32..Anki.Vector.external_interface.NavMapQuadInfo*\xc8\x02\n\x12NavNodeContentType\x12\x14\n\x10NAV_NODE_UNKNOWN\x10\x00\x12\x1e\n\x1aNAV_NODE_CLEAR_OF_OBSTACLE\x10\x01\x12\x1b\n\x17NAV_NODE_CLEAR_OF_CLIFF\x10\x02\x12\x1a\n\x16NAV_NODE_OBSTACLE_CUBE\x10\x03\x12\x1f\n\x1bNAV_NODE_OBSTACLE_PROXIMITY\x10\x04\x12(\n$NAV_NODE_OBSTACLE_PROXIMITY_EXPLORED\x10\x05\x12\"\n\x1eNAV_NODE_OBSTACLE_UNRECOGNIZED\x10\x06\x12\x12\n\x0eNAV_NODE_CLIFF\x10\x07\x12\x1d\n\x19NAV_NODE_INTERESTING_EDGE\x10\x08\x12!\n\x1dNAV_NODE_NON_INTERESTING_EDGE\x10\tb\x06proto3')
)

_NAVNODECONTENTTYPE = _descriptor.EnumDescriptor(
  name='NavNodeContentType',
  full_name='Anki.Vector.external_interface.NavNodeContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_CLEAR_OF_OBSTACLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_CLEAR_OF_CLIFF', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_OBSTACLE_CUBE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_OBSTACLE_PROXIMITY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_OBSTACLE_PROXIMITY_EXPLORED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_OBSTACLE_UNRECOGNIZED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_CLIFF', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_INTERESTING_EDGE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAV_NODE_NON_INTERESTING_EDGE', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=531,
  serialized_end=859,
)
_sym_db.RegisterEnumDescriptor(_NAVNODECONTENTTYPE)

NavNodeContentType = enum_type_wrapper.EnumTypeWrapper(_NAVNODECONTENTTYPE)
NAV_NODE_UNKNOWN = 0
NAV_NODE_CLEAR_OF_OBSTACLE = 1
NAV_NODE_CLEAR_OF_CLIFF = 2
NAV_NODE_OBSTACLE_CUBE = 3
NAV_NODE_OBSTACLE_PROXIMITY = 4
NAV_NODE_OBSTACLE_PROXIMITY_EXPLORED = 5
NAV_NODE_OBSTACLE_UNRECOGNIZED = 6
NAV_NODE_CLIFF = 7
NAV_NODE_INTERESTING_EDGE = 8
NAV_NODE_NON_INTERESTING_EDGE = 9



_NAVMAPQUADINFO = _descriptor.Descriptor(
  name='NavMapQuadInfo',
  full_name='Anki.Vector.external_interface.NavMapQuadInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='Anki.Vector.external_interface.NavMapQuadInfo.content', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='Anki.Vector.external_interface.NavMapQuadInfo.depth', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_rgba', full_name='Anki.Vector.external_interface.NavMapQuadInfo.color_rgba', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  ],
  serialized_start=71,
  serialized_end=191,
)


_NAVMAPINFO = _descriptor.Descriptor(
  name='NavMapInfo',
  full_name='Anki.Vector.external_interface.NavMapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_depth', full_name='Anki.Vector.external_interface.NavMapInfo.root_depth', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_size_mm', full_name='Anki.Vector.external_interface.NavMapInfo.root_size_mm', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_center_x', full_name='Anki.Vector.external_interface.NavMapInfo.root_center_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_center_y', full_name='Anki.Vector.external_interface.NavMapInfo.root_center_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_center_z', full_name='Anki.Vector.external_interface.NavMapInfo.root_center_z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  ],
  serialized_start=193,
  serialized_end=316,
)


_NAVMAPFEEDREQUEST = _descriptor.Descriptor(
  name='NavMapFeedRequest',
  full_name='Anki.Vector.external_interface.NavMapFeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='Anki.Vector.external_interface.NavMapFeedRequest.frequency', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  ],
  serialized_start=318,
  serialized_end=356,
)


_NAVMAPFEEDRESPONSE = _descriptor.Descriptor(
  name='NavMapFeedResponse',
  full_name='Anki.Vector.external_interface.NavMapFeedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='Anki.Vector.external_interface.NavMapFeedResponse.origin_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_info', full_name='Anki.Vector.external_interface.NavMapFeedResponse.map_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quad_infos', full_name='Anki.Vector.external_interface.NavMapFeedResponse.quad_infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=359,
  serialized_end=528,
)

_NAVMAPQUADINFO.fields_by_name['content'].enum_type = _NAVNODECONTENTTYPE
_NAVMAPFEEDRESPONSE.fields_by_name['map_info'].message_type = _NAVMAPINFO
_NAVMAPFEEDRESPONSE.fields_by_name['quad_infos'].message_type = _NAVMAPQUADINFO
DESCRIPTOR.message_types_by_name['NavMapQuadInfo'] = _NAVMAPQUADINFO
DESCRIPTOR.message_types_by_name['NavMapInfo'] = _NAVMAPINFO
DESCRIPTOR.message_types_by_name['NavMapFeedRequest'] = _NAVMAPFEEDREQUEST
DESCRIPTOR.message_types_by_name['NavMapFeedResponse'] = _NAVMAPFEEDRESPONSE
DESCRIPTOR.enum_types_by_name['NavNodeContentType'] = _NAVNODECONTENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NavMapQuadInfo = _reflection.GeneratedProtocolMessageType('NavMapQuadInfo', (_message.Message,), dict(
  DESCRIPTOR = _NAVMAPQUADINFO,
  __module__ = 'anki_vector.messaging.nav_map_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.NavMapQuadInfo)
  ))
_sym_db.RegisterMessage(NavMapQuadInfo)

NavMapInfo = _reflection.GeneratedProtocolMessageType('NavMapInfo', (_message.Message,), dict(
  DESCRIPTOR = _NAVMAPINFO,
  __module__ = 'anki_vector.messaging.nav_map_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.NavMapInfo)
  ))
_sym_db.RegisterMessage(NavMapInfo)

NavMapFeedRequest = _reflection.GeneratedProtocolMessageType('NavMapFeedRequest', (_message.Message,), dict(
  DESCRIPTOR = _NAVMAPFEEDREQUEST,
  __module__ = 'anki_vector.messaging.nav_map_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.NavMapFeedRequest)
  ))
_sym_db.RegisterMessage(NavMapFeedRequest)

NavMapFeedResponse = _reflection.GeneratedProtocolMessageType('NavMapFeedResponse', (_message.Message,), dict(
  DESCRIPTOR = _NAVMAPFEEDRESPONSE,
  __module__ = 'anki_vector.messaging.nav_map_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.NavMapFeedResponse)
  ))
_sym_db.RegisterMessage(NavMapFeedResponse)


# @@protoc_insertion_point(module_scope)
