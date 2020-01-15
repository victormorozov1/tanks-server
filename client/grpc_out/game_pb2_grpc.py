# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import game_server.grpc_out.game_pb2 as game__pb2


class GameStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.unary_unary(
        '/grpc.Game/Connect',
        request_serializer=game__pb2.PlayerInformation.SerializeToString,
        response_deserializer=game__pb2.Nothing.FromString,
        )
    self.GetMap = channel.unary_unary(
        '/grpc.Game/GetMap',
        request_serializer=game__pb2.Nothing.SerializeToString,
        response_deserializer=game__pb2.Map.FromString,
        )
    self.GetPlayersMovements = channel.unary_stream(
        '/grpc.Game/GetPlayersMovements',
        request_serializer=game__pb2.Nothing.SerializeToString,
        response_deserializer=game__pb2.PlayerMovement.FromString,
        )
    self.GetPlayersTurns = channel.unary_stream(
        '/grpc.Game/GetPlayersTurns',
        request_serializer=game__pb2.Nothing.SerializeToString,
        response_deserializer=game__pb2.PlayerTurn.FromString,
        )
    self.GetPlayersShots = channel.unary_stream(
        '/grpc.Game/GetPlayersShots',
        request_serializer=game__pb2.Nothing.SerializeToString,
        response_deserializer=game__pb2.Id.FromString,
        )
    self.Move = channel.unary_unary(
        '/grpc.Game/Move',
        request_serializer=game__pb2.Movement.SerializeToString,
        response_deserializer=game__pb2.Nothing.FromString,
        )
    self.Turn = channel.unary_unary(
        '/grpc.Game/Turn',
        request_serializer=game__pb2.Direction.SerializeToString,
        response_deserializer=game__pb2.Nothing.FromString,
        )
    self.Fire = channel.unary_unary(
        '/grpc.Game/Fire',
        request_serializer=game__pb2.Nothing.SerializeToString,
        response_deserializer=game__pb2.Nothing.FromString,
        )


class GameServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Connect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMap(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayersMovements(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayersTurns(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayersShots(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Turn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fire(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GameServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=game__pb2.PlayerInformation.FromString,
          response_serializer=game__pb2.Nothing.SerializeToString,
      ),
      'GetMap': grpc.unary_unary_rpc_method_handler(
          servicer.GetMap,
          request_deserializer=game__pb2.Nothing.FromString,
          response_serializer=game__pb2.Map.SerializeToString,
      ),
      'GetPlayersMovements': grpc.unary_stream_rpc_method_handler(
          servicer.GetPlayersMovements,
          request_deserializer=game__pb2.Nothing.FromString,
          response_serializer=game__pb2.PlayerMovement.SerializeToString,
      ),
      'GetPlayersTurns': grpc.unary_stream_rpc_method_handler(
          servicer.GetPlayersTurns,
          request_deserializer=game__pb2.Nothing.FromString,
          response_serializer=game__pb2.PlayerTurn.SerializeToString,
      ),
      'GetPlayersShots': grpc.unary_stream_rpc_method_handler(
          servicer.GetPlayersShots,
          request_deserializer=game__pb2.Nothing.FromString,
          response_serializer=game__pb2.Id.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=game__pb2.Movement.FromString,
          response_serializer=game__pb2.Nothing.SerializeToString,
      ),
      'Turn': grpc.unary_unary_rpc_method_handler(
          servicer.Turn,
          request_deserializer=game__pb2.Direction.FromString,
          response_serializer=game__pb2.Nothing.SerializeToString,
      ),
      'Fire': grpc.unary_unary_rpc_method_handler(
          servicer.Fire,
          request_deserializer=game__pb2.Nothing.FromString,
          response_serializer=game__pb2.Nothing.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.Game', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
