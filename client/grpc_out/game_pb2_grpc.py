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
    self.Stream = channel.stream_stream(
        '/grpc.Game/Stream',
        request_serializer=game__pb2.Command.SerializeToString,
        response_deserializer=game__pb2.ServerMessage.FromString,
        )


class GameServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Stream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GameServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Stream': grpc.stream_stream_rpc_method_handler(
          servicer.Stream,
          request_deserializer=game__pb2.Command.FromString,
          response_serializer=game__pb2.ServerMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.Game', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
