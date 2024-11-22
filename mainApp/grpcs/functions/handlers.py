from concurrent import futures
import grpc
from ..files import aiguard_pb2_grpc
from .services import AiGuardService

def grpc_handlers(server):
    """
    Registers gRPC handlers with the server.
    """
    aiguard_pb2_grpc.add_AiGuardServicer_to_server(AiGuardService(), server)
