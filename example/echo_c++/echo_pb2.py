# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\necho.proto\x12\x07\x65xample\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x02(\t2B\n\x0b\x45\x63hoService\x12\x33\n\x04\x45\x63ho\x12\x14.example.EchoRequest\x1a\x15.example.EchoResponseB\x03\x80\x01\x01')



_ECHOREQUEST = DESCRIPTOR.message_types_by_name['EchoRequest']
_ECHORESPONSE = DESCRIPTOR.message_types_by_name['EchoResponse']
EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:example.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ECHORESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:example.EchoResponse)
  })
_sym_db.RegisterMessage(EchoResponse)

_ECHOSERVICE = DESCRIPTOR.services_by_name['EchoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _ECHOREQUEST._serialized_start=23
  _ECHOREQUEST._serialized_end=53
  _ECHORESPONSE._serialized_start=55
  _ECHORESPONSE._serialized_end=86
  _ECHOSERVICE._serialized_start=88
  _ECHOSERVICE._serialized_end=154
# @@protoc_insertion_point(module_scope)
