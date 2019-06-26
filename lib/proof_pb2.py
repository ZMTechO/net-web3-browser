# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proof.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import transaction_info_pb2 as transaction__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proof.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bproof.proto\x12\x05types\x1a\x16transaction_info.proto\"@\n\x10\x41\x63\x63umulatorProof\x12\x0e\n\x06\x62itmap\x18\x01 \x01(\x04\x12\x1c\n\x14non_default_siblings\x18\x02 \x03(\x0c\"O\n\x11SparseMerkleProof\x12\x0c\n\x04leaf\x18\x01 \x01(\x0c\x12\x0e\n\x06\x62itmap\x18\x02 \x01(\x0c\x12\x1c\n\x14non_default_siblings\x18\x03 \x03(\x0c\"\x92\x01\n\x16SignedTransactionProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\"\xd2\x01\n\x11\x41\x63\x63ountStateProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\x12\x43\n!transaction_info_to_account_proof\x18\x03 \x01(\x0b\x32\x18.types.SparseMerkleProof\"\xc8\x01\n\nEventProof\x12\x46\n%ledger_info_to_transaction_info_proof\x18\x01 \x01(\x0b\x32\x17.types.AccumulatorProof\x12\x30\n\x10transaction_info\x18\x02 \x01(\x0b\x32\x16.types.TransactionInfo\x12@\n\x1ftransaction_info_to_event_proof\x18\x03 \x01(\x0b\x32\x17.types.AccumulatorProofb\x06proto3')
  ,
  dependencies=[transaction__info__pb2.DESCRIPTOR,])




_ACCUMULATORPROOF = _descriptor.Descriptor(
  name='AccumulatorProof',
  full_name='types.AccumulatorProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bitmap', full_name='types.AccumulatorProof.bitmap', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='non_default_siblings', full_name='types.AccumulatorProof.non_default_siblings', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=46,
  serialized_end=110,
)


_SPARSEMERKLEPROOF = _descriptor.Descriptor(
  name='SparseMerkleProof',
  full_name='types.SparseMerkleProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf', full_name='types.SparseMerkleProof.leaf', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitmap', full_name='types.SparseMerkleProof.bitmap', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='non_default_siblings', full_name='types.SparseMerkleProof.non_default_siblings', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=112,
  serialized_end=191,
)


_SIGNEDTRANSACTIONPROOF = _descriptor.Descriptor(
  name='SignedTransactionProof',
  full_name='types.SignedTransactionProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.SignedTransactionProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.SignedTransactionProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=340,
)


_ACCOUNTSTATEPROOF = _descriptor.Descriptor(
  name='AccountStateProof',
  full_name='types.AccountStateProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.AccountStateProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.AccountStateProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info_to_account_proof', full_name='types.AccountStateProof.transaction_info_to_account_proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=343,
  serialized_end=553,
)


_EVENTPROOF = _descriptor.Descriptor(
  name='EventProof',
  full_name='types.EventProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_to_transaction_info_proof', full_name='types.EventProof.ledger_info_to_transaction_info_proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info', full_name='types.EventProof.transaction_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_info_to_event_proof', full_name='types.EventProof.transaction_info_to_event_proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=556,
  serialized_end=756,
)

_SIGNEDTRANSACTIONPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_SIGNEDTRANSACTIONPROOF.fields_by_name['transaction_info'].message_type = transaction__info__pb2._TRANSACTIONINFO
_ACCOUNTSTATEPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_ACCOUNTSTATEPROOF.fields_by_name['transaction_info'].message_type = transaction__info__pb2._TRANSACTIONINFO
_ACCOUNTSTATEPROOF.fields_by_name['transaction_info_to_account_proof'].message_type = _SPARSEMERKLEPROOF
_EVENTPROOF.fields_by_name['ledger_info_to_transaction_info_proof'].message_type = _ACCUMULATORPROOF
_EVENTPROOF.fields_by_name['transaction_info'].message_type = transaction__info__pb2._TRANSACTIONINFO
_EVENTPROOF.fields_by_name['transaction_info_to_event_proof'].message_type = _ACCUMULATORPROOF
DESCRIPTOR.message_types_by_name['AccumulatorProof'] = _ACCUMULATORPROOF
DESCRIPTOR.message_types_by_name['SparseMerkleProof'] = _SPARSEMERKLEPROOF
DESCRIPTOR.message_types_by_name['SignedTransactionProof'] = _SIGNEDTRANSACTIONPROOF
DESCRIPTOR.message_types_by_name['AccountStateProof'] = _ACCOUNTSTATEPROOF
DESCRIPTOR.message_types_by_name['EventProof'] = _EVENTPROOF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccumulatorProof = _reflection.GeneratedProtocolMessageType('AccumulatorProof', (_message.Message,), dict(
  DESCRIPTOR = _ACCUMULATORPROOF,
  __module__ = 'proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccumulatorProof)
  ))
_sym_db.RegisterMessage(AccumulatorProof)

SparseMerkleProof = _reflection.GeneratedProtocolMessageType('SparseMerkleProof', (_message.Message,), dict(
  DESCRIPTOR = _SPARSEMERKLEPROOF,
  __module__ = 'proof_pb2'
  # @@protoc_insertion_point(class_scope:types.SparseMerkleProof)
  ))
_sym_db.RegisterMessage(SparseMerkleProof)

SignedTransactionProof = _reflection.GeneratedProtocolMessageType('SignedTransactionProof', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDTRANSACTIONPROOF,
  __module__ = 'proof_pb2'
  # @@protoc_insertion_point(class_scope:types.SignedTransactionProof)
  ))
_sym_db.RegisterMessage(SignedTransactionProof)

AccountStateProof = _reflection.GeneratedProtocolMessageType('AccountStateProof', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTSTATEPROOF,
  __module__ = 'proof_pb2'
  # @@protoc_insertion_point(class_scope:types.AccountStateProof)
  ))
_sym_db.RegisterMessage(AccountStateProof)

EventProof = _reflection.GeneratedProtocolMessageType('EventProof', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPROOF,
  __module__ = 'proof_pb2'
  # @@protoc_insertion_point(class_scope:types.EventProof)
  ))
_sym_db.RegisterMessage(EventProof)


# @@protoc_insertion_point(module_scope)
