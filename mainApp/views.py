from django.http import JsonResponse
from .grpcs.functions.grpc_run_logic import grpc_run_logic


def grpc_http_handler(request):
    """
    HTTP endpoint to process data and forward it to AiGuard gRPC service.
    """
    # Example input data (could also come from POST request body, etc.)
    incoming_data = [
        {
            "timestamp": "2024-11-21T15:30:00Z",
            "source_ip": "192.168.1.1",
            "source_port": 8080,
            "country": "US",
            "asn": "AS12345",
            "org": "Some Organization",
            "blacklist": 0,
            "original_url": "https://example.com",
            "user_agent": "Mozilla/5.0",
            "headers": {"Content-Type": "application/json"},
            "method": "GET",
            "query": {"key1": "value1", "key2": "value2"},
            "cookies": "cookie1=value1; cookie2=value2"
        },
        # Add more objects to test multiple requests
    ]

    # Call the gRPC logic
    result = grpc_run_logic(incoming_data)
    return JsonResponse(result, safe=False)
