# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/grpc_out/game.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/grpc_out/game.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63lient/grpc_out/game.proto\x12\x04grpc\"\t\n\x07Nothing\"\x10\n\x03Map\x12\t\n\x01s\x18\x01 \x01(\t\"G\n\x11PlayerInformation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03szx\x18\x02 \x01(\x05\x12\x0b\n\x03szy\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\"6\n\x0fGameInformation\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05\x66ield\x18\x03 \x01(\t\"2\n\x04Move\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06move_x\x18\x02 \x01(\x05\x12\x0e\n\x06move_y\x18\x03 \x01(\x05\"\x0f\n\x02Id\x12\t\n\x01s\x18\x01 \x01(\t\"\x1a\n\x08Movement\x12\x0e\n\x06moving\x18\x01 \x01(\x08\",\n\x0bTurnMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tdirection\x18\x02 \x01(\t\":\n\x0ePlayerMovement\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05new_x\x18\x02 \x01(\x05\x12\r\n\x05new_y\x18\x03 \x01(\x05\"+\n\nPlayerTurn\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tdirection\x18\x02 \x01(\t\"\x1d\n\x10PlayersPositions\x12\t\n\x01s\x18\x01 \x01(\t\"\x14\n\x07\x42ullets\x12\t\n\x01s\x18\x01 \x01(\t\"3\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x11\n\tdirection\x18\x03 \x01(\t\"K\n\x16OtherPlayerInformation\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\x0f\n\x07healths\x18\x04 \x01(\x05\"-\n\x0fHealthsChanging\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x63hange\x18\x02 \x01(\x05\"\x11\n\x04Name\x12\t\n\x01s\x18\x01 \x01(\t2\x8c\x04\n\x04Game\x12\x32\n\x07\x43onnect\x12\x17.grpc.PlayerInformation\x1a\x0e.grpc.Position\x12\"\n\x06GetMap\x12\r.grpc.Nothing\x1a\t.grpc.Map\x12\x37\n\x13GetPlayersMovements\x12\x08.grpc.Id\x1a\x14.grpc.PlayerMovement0\x01\x12/\n\x0fGetPlayersTurns\x12\x08.grpc.Id\x1a\x10.grpc.PlayerTurn0\x01\x12/\n\rGetAllBullets\x12\r.grpc.Nothing\x1a\r.grpc.Bullets0\x01\x12>\n\rGetAllPlayers\x12\r.grpc.Nothing\x1a\x1c.grpc.OtherPlayerInformation0\x01\x12>\n\x19GetPlayersHealthsChanging\x12\x08.grpc.Id\x1a\x15.grpc.HealthsChanging0\x01\x12%\n\rGetPlayerName\x12\x08.grpc.Id\x1a\n.grpc.Name\x12\x1f\n\x04Move\x12\x08.grpc.Id\x1a\r.grpc.Nothing\x12(\n\x04Turn\x12\x11.grpc.TurnMessage\x1a\r.grpc.Nothing\x12\x1f\n\x04\x46ire\x12\x08.grpc.Id\x1a\r.grpc.Nothingb\x06proto3')
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
  serialized_start=36,
  serialized_end=45,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='grpc.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='grpc.Map.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=63,
)


_PLAYERINFORMATION = _descriptor.Descriptor(
  name='PlayerInformation',
  full_name='grpc.PlayerInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.PlayerInformation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='szx', full_name='grpc.PlayerInformation.szx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='szy', full_name='grpc.PlayerInformation.szy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.PlayerInformation.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=65,
  serialized_end=136,
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
  serialized_start=138,
  serialized_end=192,
)


_MOVE = _descriptor.Descriptor(
  name='Move',
  full_name='grpc.Move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.Move.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_x', full_name='grpc.Move.move_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_y', full_name='grpc.Move.move_y', index=2,
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
  serialized_start=194,
  serialized_end=244,
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
  serialized_start=246,
  serialized_end=261,
)


_MOVEMENT = _descriptor.Descriptor(
  name='Movement',
  full_name='grpc.Movement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='moving', full_name='grpc.Movement.moving', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=263,
  serialized_end=289,
)


_TURNMESSAGE = _descriptor.Descriptor(
  name='TurnMessage',
  full_name='grpc.TurnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.TurnMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='grpc.TurnMessage.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=291,
  serialized_end=335,
)


_PLAYERMOVEMENT = _descriptor.Descriptor(
  name='PlayerMovement',
  full_name='grpc.PlayerMovement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.PlayerMovement.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_x', full_name='grpc.PlayerMovement.new_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_y', full_name='grpc.PlayerMovement.new_y', index=2,
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
  serialized_start=337,
  serialized_end=395,
)


_PLAYERTURN = _descriptor.Descriptor(
  name='PlayerTurn',
  full_name='grpc.PlayerTurn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.PlayerTurn.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='grpc.PlayerTurn.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=397,
  serialized_end=440,
)


_PLAYERSPOSITIONS = _descriptor.Descriptor(
  name='PlayersPositions',
  full_name='grpc.PlayersPositions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='grpc.PlayersPositions.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=442,
  serialized_end=471,
)


_BULLETS = _descriptor.Descriptor(
  name='Bullets',
  full_name='grpc.Bullets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='grpc.Bullets.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=473,
  serialized_end=493,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='grpc.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='grpc.Position.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='grpc.Position.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='grpc.Position.direction', index=2,
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
  serialized_start=495,
  serialized_end=546,
)


_OTHERPLAYERINFORMATION = _descriptor.Descriptor(
  name='OtherPlayerInformation',
  full_name='grpc.OtherPlayerInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.OtherPlayerInformation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='grpc.OtherPlayerInformation.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='grpc.OtherPlayerInformation.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='healths', full_name='grpc.OtherPlayerInformation.healths', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=548,
  serialized_end=623,
)


_HEALTHSCHANGING = _descriptor.Descriptor(
  name='HealthsChanging',
  full_name='grpc.HealthsChanging',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.HealthsChanging.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change', full_name='grpc.HealthsChanging.change', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=625,
  serialized_end=670,
)


_NAME = _descriptor.Descriptor(
  name='Name',
  full_name='grpc.Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='grpc.Name.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=672,
  serialized_end=689,
)

DESCRIPTOR.message_types_by_name['Nothing'] = _NOTHING
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['PlayerInformation'] = _PLAYERINFORMATION
DESCRIPTOR.message_types_by_name['GameInformation'] = _GAMEINFORMATION
DESCRIPTOR.message_types_by_name['Move'] = _MOVE
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Movement'] = _MOVEMENT
DESCRIPTOR.message_types_by_name['TurnMessage'] = _TURNMESSAGE
DESCRIPTOR.message_types_by_name['PlayerMovement'] = _PLAYERMOVEMENT
DESCRIPTOR.message_types_by_name['PlayerTurn'] = _PLAYERTURN
DESCRIPTOR.message_types_by_name['PlayersPositions'] = _PLAYERSPOSITIONS
DESCRIPTOR.message_types_by_name['Bullets'] = _BULLETS
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['OtherPlayerInformation'] = _OTHERPLAYERINFORMATION
DESCRIPTOR.message_types_by_name['HealthsChanging'] = _HEALTHSCHANGING
DESCRIPTOR.message_types_by_name['Name'] = _NAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nothing = _reflection.GeneratedProtocolMessageType('Nothing', (_message.Message,), {
  'DESCRIPTOR' : _NOTHING,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Nothing)
  })
_sym_db.RegisterMessage(Nothing)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Map)
  })
_sym_db.RegisterMessage(Map)

PlayerInformation = _reflection.GeneratedProtocolMessageType('PlayerInformation', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERINFORMATION,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.PlayerInformation)
  })
_sym_db.RegisterMessage(PlayerInformation)

GameInformation = _reflection.GeneratedProtocolMessageType('GameInformation', (_message.Message,), {
  'DESCRIPTOR' : _GAMEINFORMATION,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.GameInformation)
  })
_sym_db.RegisterMessage(GameInformation)

Move = _reflection.GeneratedProtocolMessageType('Move', (_message.Message,), {
  'DESCRIPTOR' : _MOVE,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Move)
  })
_sym_db.RegisterMessage(Move)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Id)
  })
_sym_db.RegisterMessage(Id)

Movement = _reflection.GeneratedProtocolMessageType('Movement', (_message.Message,), {
  'DESCRIPTOR' : _MOVEMENT,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Movement)
  })
_sym_db.RegisterMessage(Movement)

TurnMessage = _reflection.GeneratedProtocolMessageType('TurnMessage', (_message.Message,), {
  'DESCRIPTOR' : _TURNMESSAGE,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.TurnMessage)
  })
_sym_db.RegisterMessage(TurnMessage)

PlayerMovement = _reflection.GeneratedProtocolMessageType('PlayerMovement', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERMOVEMENT,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.PlayerMovement)
  })
_sym_db.RegisterMessage(PlayerMovement)

PlayerTurn = _reflection.GeneratedProtocolMessageType('PlayerTurn', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERTURN,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.PlayerTurn)
  })
_sym_db.RegisterMessage(PlayerTurn)

PlayersPositions = _reflection.GeneratedProtocolMessageType('PlayersPositions', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSPOSITIONS,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.PlayersPositions)
  })
_sym_db.RegisterMessage(PlayersPositions)

Bullets = _reflection.GeneratedProtocolMessageType('Bullets', (_message.Message,), {
  'DESCRIPTOR' : _BULLETS,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Bullets)
  })
_sym_db.RegisterMessage(Bullets)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Position)
  })
_sym_db.RegisterMessage(Position)

OtherPlayerInformation = _reflection.GeneratedProtocolMessageType('OtherPlayerInformation', (_message.Message,), {
  'DESCRIPTOR' : _OTHERPLAYERINFORMATION,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.OtherPlayerInformation)
  })
_sym_db.RegisterMessage(OtherPlayerInformation)

HealthsChanging = _reflection.GeneratedProtocolMessageType('HealthsChanging', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHSCHANGING,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.HealthsChanging)
  })
_sym_db.RegisterMessage(HealthsChanging)

Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), {
  'DESCRIPTOR' : _NAME,
  '__module__' : 'client.grpc_out.game_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Name)
  })
_sym_db.RegisterMessage(Name)



_GAME = _descriptor.ServiceDescriptor(
  name='Game',
  full_name='grpc.Game',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=692,
  serialized_end=1216,
  methods=[
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='grpc.Game.Connect',
    index=0,
    containing_service=None,
    input_type=_PLAYERINFORMATION,
    output_type=_POSITION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMap',
    full_name='grpc.Game.GetMap',
    index=1,
    containing_service=None,
    input_type=_NOTHING,
    output_type=_MAP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayersMovements',
    full_name='grpc.Game.GetPlayersMovements',
    index=2,
    containing_service=None,
    input_type=_ID,
    output_type=_PLAYERMOVEMENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayersTurns',
    full_name='grpc.Game.GetPlayersTurns',
    index=3,
    containing_service=None,
    input_type=_ID,
    output_type=_PLAYERTURN,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllBullets',
    full_name='grpc.Game.GetAllBullets',
    index=4,
    containing_service=None,
    input_type=_NOTHING,
    output_type=_BULLETS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllPlayers',
    full_name='grpc.Game.GetAllPlayers',
    index=5,
    containing_service=None,
    input_type=_NOTHING,
    output_type=_OTHERPLAYERINFORMATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayersHealthsChanging',
    full_name='grpc.Game.GetPlayersHealthsChanging',
    index=6,
    containing_service=None,
    input_type=_ID,
    output_type=_HEALTHSCHANGING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayerName',
    full_name='grpc.Game.GetPlayerName',
    index=7,
    containing_service=None,
    input_type=_ID,
    output_type=_NAME,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Move',
    full_name='grpc.Game.Move',
    index=8,
    containing_service=None,
    input_type=_ID,
    output_type=_NOTHING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Turn',
    full_name='grpc.Game.Turn',
    index=9,
    containing_service=None,
    input_type=_TURNMESSAGE,
    output_type=_NOTHING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Fire',
    full_name='grpc.Game.Fire',
    index=10,
    containing_service=None,
    input_type=_ID,
    output_type=_NOTHING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAME)

DESCRIPTOR.services_by_name['Game'] = _GAME

# @@protoc_insertion_point(module_scope)
