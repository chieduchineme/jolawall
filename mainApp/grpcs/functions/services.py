from ..files import aiguard_pb2_grpc
from ..files import aiguard_pb2

class AiGuardService(aiguard_pb2_grpc.AiGuardServicer):
    def HandleHttpRequest(self, request, context):
        """
        Handles incoming HTTP request gRPC calls.
        """
        # Access the request data (e.g., common params, params)
        common_params = request.common
        http_params = request.params

        # Example response
        confidence = 0.95  # Dummy confidence score
        columns = ["column1", "column2"]  # Dummy columns

        return aiguard_pb2.AiGuardResponse(confidence=confidence, columns=columns)
