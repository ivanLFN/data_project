from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer



# curl -X POST -H "Content-Type: application/json" -d '{"username":"myuser", "password":"mypassword", "email":"user@example.com"}' http://127.0.0.1:8000/register/
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


