from rest_framework.response import Response
from rest_framework import status

def custom_response(success=True, message=None, data=None, status_code=status.HTTP_200_OK):
    """
    Standard response format for all APIs
    """
    return Response({
        "status": "success" if success else "error",
        "message": message or ("Operation successful" if success else "Operation failed"),
        "data": data if data is not None else []
    }, status=status_code)