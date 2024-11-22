import grpc
from ..files.aiguard_pb2 import AiGuardHttpRequest, AiGuardHttpRequestParams, AiGuardCommonParams
from ..files.aiguard_pb2_grpc import AiGuardStub
from ..files.genericval_pb2 import AppGuardGenericVal  # Assuming this is generated from `genericval.proto`


def grpc_run_logic(data_array):
    """
    Sends an array of HTTP request objects to the AiGuard gRPC server and retrieves responses.

    :param data_array: List of dictionaries containing HTTP request data.
    :return: List of responses from the AiGuard service.
    """
    # Initialize gRPC channel and stub
    channel = grpc.insecure_channel('localhost:50052')
    stub = AiGuardStub(channel)

    try:
        # Prepare the gRPC requests
        requests = []
        for data in data_array:
            # Create HTTP request parameters
            params = AiGuardHttpRequestParams(
                original_url=data.get("original_url", ""),
                user_agent=AppGuardGenericVal(string_val=data.get("user_agent", "")),
                headers={
                    key: AppGuardGenericVal(string_val=value)
                    for key, value in data.get("headers", {}).items()
                },
                method=data.get("method", ""),
                query={
                    key: AppGuardGenericVal(string_val=value)
                    for key, value in data.get("query", {}).items()
                },
                cookies=AppGuardGenericVal(string_val=data.get("cookies", "")),
            )

            # Create common parameters
            common = AiGuardCommonParams(
                timestamp=data.get("timestamp", ""),
                source_ip=data.get("source_ip", ""),
                source_port=data.get("source_port", 0),
                country=data.get("country", ""),
                asn=data.get("asn", ""),
                org=data.get("org", ""),
                blacklist=data.get("blacklist", 0),
            )

            # Add the full HTTP request to the request list
            requests.append(AiGuardHttpRequest(common=common, params=params))

        # Send requests to the gRPC service and collect responses
        responses = []
        for request in requests:
            response = stub.HandleHttpRequest(request)
            responses.append({
                "confidence": response.confidence,
                "columns": list(response.columns)
            })

        return responses

    except grpc.RpcError as e:
        # Handle gRPC errors
        return {"error": f"gRPC Error: {e.details()}"}
    finally:
        channel.close()
