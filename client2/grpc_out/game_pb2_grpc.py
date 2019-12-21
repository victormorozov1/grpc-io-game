# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import client.grpc_out.game_pb2 as game__pb2


class GameStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetField = channel.unary_stream(
        '/grpc.Game/GetField',
        request_serializer=game__pb2.Id.SerializeToString,
        response_deserializer=game__pb2.GameInformation.FromString,
        )
    self.MakeStep = channel.unary_unary(
        '/grpc.Game/MakeStep',
        request_serializer=game__pb2.Step.SerializeToString,
        response_deserializer=game__pb2.Nothing.FromString,
        )


class GameServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetField(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MakeStep(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GameServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetField': grpc.unary_stream_rpc_method_handler(
          servicer.GetField,
          request_deserializer=game__pb2.Id.FromString,
          response_serializer=game__pb2.GameInformation.SerializeToString,
      ),
      'MakeStep': grpc.unary_unary_rpc_method_handler(
          servicer.MakeStep,
          request_deserializer=game__pb2.Step.FromString,
          response_serializer=game__pb2.Nothing.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.Game', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
