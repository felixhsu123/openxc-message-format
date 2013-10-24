# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openxc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openxc.proto',
  package='openxc',
  serialized_pb='\n\x0copenxc.proto\x12\x06openxc\"\x9a\x04\n\x0eVehicleMessage\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.VehicleMessage.Type\x12\'\n\x0braw_message\x18\x02 \x01(\x0b\x32\x12.openxc.RawMessage\x12-\n\x0estring_message\x18\x03 \x01(\x0b\x32\x15.openxc.StringMessage\x12/\n\x0fnumeric_message\x18\x04 \x01(\x0b\x32\x16.openxc.NumericMessage\x12/\n\x0f\x62oolean_message\x18\x05 \x01(\x0b\x32\x16.openxc.BooleanMessage\x12<\n\x16\x65vented_string_message\x18\x06 \x01(\x0b\x32\x1c.openxc.EventedStringMessage\x12>\n\x17\x65vented_boolean_message\x18\x07 \x01(\x0b\x32\x1d.openxc.EventedBooleanMessage\x12>\n\x17\x65vented_numeric_message\x18\x08 \x01(\x0b\x32\x1d.openxc.EventedNumericMessage\"e\n\x04Type\x12\x07\n\x03RAW\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\x07\n\x03NUM\x10\x04\x12\x0f\n\x0b\x45VENTED_NUM\x10\x05\x12\x12\n\x0e\x45VENTED_STRING\x10\x06\x12\x10\n\x0c\x45VENTED_BOOL\x10\x07\"-\n\nRawMessage\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\",\n\rStringMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"-\n\x0eNumericMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"-\n\x0e\x42ooleanMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\"B\n\x14\x45ventedStringMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\t\"C\n\x15\x45ventedBooleanMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\x08\"C\n\x15\x45ventedNumericMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\x01\x42\x1c\n\ncom.openxcB\x0e\x42inaryMessages')



_VEHICLEMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.VehicleMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_NUM', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_STRING', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_BOOL', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=462,
  serialized_end=563,
)


_VEHICLEMESSAGE = _descriptor.Descriptor(
  name='VehicleMessage',
  full_name='openxc.VehicleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.VehicleMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_message', full_name='openxc.VehicleMessage.raw_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_message', full_name='openxc.VehicleMessage.string_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_message', full_name='openxc.VehicleMessage.numeric_message', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_message', full_name='openxc.VehicleMessage.boolean_message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evented_string_message', full_name='openxc.VehicleMessage.evented_string_message', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evented_boolean_message', full_name='openxc.VehicleMessage.evented_boolean_message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evented_numeric_message', full_name='openxc.VehicleMessage.evented_numeric_message', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=25,
  serialized_end=563,
)


_RAWMESSAGE = _descriptor.Descriptor(
  name='RawMessage',
  full_name='openxc.RawMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.RawMessage.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.RawMessage.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=565,
  serialized_end=610,
)


_STRINGMESSAGE = _descriptor.Descriptor(
  name='StringMessage',
  full_name='openxc.StringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.StringMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.StringMessage.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=612,
  serialized_end=656,
)


_NUMERICMESSAGE = _descriptor.Descriptor(
  name='NumericMessage',
  full_name='openxc.NumericMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.NumericMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.NumericMessage.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=658,
  serialized_end=703,
)


_BOOLEANMESSAGE = _descriptor.Descriptor(
  name='BooleanMessage',
  full_name='openxc.BooleanMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.BooleanMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.BooleanMessage.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=705,
  serialized_end=750,
)


_EVENTEDSTRINGMESSAGE = _descriptor.Descriptor(
  name='EventedStringMessage',
  full_name='openxc.EventedStringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.EventedStringMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.EventedStringMessage.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='openxc.EventedStringMessage.event', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=752,
  serialized_end=818,
)


_EVENTEDBOOLEANMESSAGE = _descriptor.Descriptor(
  name='EventedBooleanMessage',
  full_name='openxc.EventedBooleanMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.EventedBooleanMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.EventedBooleanMessage.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='openxc.EventedBooleanMessage.event', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=820,
  serialized_end=887,
)


_EVENTEDNUMERICMESSAGE = _descriptor.Descriptor(
  name='EventedNumericMessage',
  full_name='openxc.EventedNumericMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.EventedNumericMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.EventedNumericMessage.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='openxc.EventedNumericMessage.event', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=889,
  serialized_end=956,
)

_VEHICLEMESSAGE.fields_by_name['type'].enum_type = _VEHICLEMESSAGE_TYPE
_VEHICLEMESSAGE.fields_by_name['raw_message'].message_type = _RAWMESSAGE
_VEHICLEMESSAGE.fields_by_name['string_message'].message_type = _STRINGMESSAGE
_VEHICLEMESSAGE.fields_by_name['numeric_message'].message_type = _NUMERICMESSAGE
_VEHICLEMESSAGE.fields_by_name['boolean_message'].message_type = _BOOLEANMESSAGE
_VEHICLEMESSAGE.fields_by_name['evented_string_message'].message_type = _EVENTEDSTRINGMESSAGE
_VEHICLEMESSAGE.fields_by_name['evented_boolean_message'].message_type = _EVENTEDBOOLEANMESSAGE
_VEHICLEMESSAGE.fields_by_name['evented_numeric_message'].message_type = _EVENTEDNUMERICMESSAGE
_VEHICLEMESSAGE_TYPE.containing_type = _VEHICLEMESSAGE;
DESCRIPTOR.message_types_by_name['VehicleMessage'] = _VEHICLEMESSAGE
DESCRIPTOR.message_types_by_name['RawMessage'] = _RAWMESSAGE
DESCRIPTOR.message_types_by_name['StringMessage'] = _STRINGMESSAGE
DESCRIPTOR.message_types_by_name['NumericMessage'] = _NUMERICMESSAGE
DESCRIPTOR.message_types_by_name['BooleanMessage'] = _BOOLEANMESSAGE
DESCRIPTOR.message_types_by_name['EventedStringMessage'] = _EVENTEDSTRINGMESSAGE
DESCRIPTOR.message_types_by_name['EventedBooleanMessage'] = _EVENTEDBOOLEANMESSAGE
DESCRIPTOR.message_types_by_name['EventedNumericMessage'] = _EVENTEDNUMERICMESSAGE

class VehicleMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VEHICLEMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.VehicleMessage)

class RawMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAWMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.RawMessage)

class StringMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRINGMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.StringMessage)

class NumericMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NUMERICMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.NumericMessage)

class BooleanMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOLEANMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.BooleanMessage)

class EventedStringMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTEDSTRINGMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.EventedStringMessage)

class EventedBooleanMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTEDBOOLEANMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.EventedBooleanMessage)

class EventedNumericMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTEDNUMERICMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.EventedNumericMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\ncom.openxcB\016BinaryMessages')
# @@protoc_insertion_point(module_scope)
