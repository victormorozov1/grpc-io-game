# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ngame.proto\x12\x04grpc\"\t\n\x07Nothing\")\n\x02Id\x12\t\n\x01s\x18\x01 \x01(\t\x12\x0b\n\x03szx\x18\x02 \x01(\x05\x12\x0b\n\x03szy\x18\x03 \x01(\x05\"6\n\x0fGameInformation\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05\x66ield\x18\x03 \x01(\t\"2\n\x04Step\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06move_x\x18\x02 \x01(\x05\x12\x0e\n\x06move_y\x18\x03 \x01(\x05\x32\\\n\x04Game\x12-\n\x08GetField\x12\x08.grpc.Id\x1a\x15.grpc.GameInformation0\x01\x12%\n\x08MakeStep\x12\n.grpc.Step\x1a\r.grpc.Nothingb\x06proto3')
)




_NOTHING = _descriptor.Descriptor(
  name='Nothing',
  full_name='grpc.Nothing',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=29,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='grpc.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='grpc.Id.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='szx', full_name='grpc.Id.szx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='szy', full_name='grpc.Id.szy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=72,
)


_GAMEINFORMATION = _descriptor.Descriptor(
  name='GameInformation',
  full_name='grpc.GameInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='grpc.GameInformation.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='grpc.GameInformation.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='grpc.GameInformation.field', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=128,
)


_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='grpc.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.Step.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_x', full_name='grpc.Step.move_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_y', full_name='grpc.Step.move_y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['Nothing'] = _NOTHING
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['GameInformation'] = _GAMEINFORMATION
DESCRIPTOR.message_types_by_name['Step'] = _STEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nothing = _reflection.GeneratedProtocolMessageType('Nothing', (_message.Message,), {
  'DESCRIPTOR' : _NOTHING,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Nothing)
  })
_sym_db.RegisterMessage(Nothing)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Id)
  })
_sym_db.RegisterMessage(Id)

GameInformation = _reflection.GeneratedProtocolMessageType('GameInformation', (_message.Message,), {
  'DESCRIPTOR' : _GAMEINFORMATION,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.GameInformation)
  })
_sym_db.RegisterMessage(GameInformation)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), {
  'DESCRIPTOR' : _STEP,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Step)
  })
_sym_db.RegisterMessage(Step)



_GAME = _descriptor.ServiceDescriptor(
  name='Game',
  full_name='grpc.Game',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=182,
  serialized_end=274,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetField',
    full_name='grpc.Game.GetField',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_GAMEINFORMATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MakeStep',
    full_name='grpc.Game.MakeStep',
    index=1,
    containing_service=None,
    input_type=_STEP,
    output_type=_NOTHING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAME)

DESCRIPTOR.services_by_name['Game'] = _GAME

# @@protoc_insertion_point(module_scope)
