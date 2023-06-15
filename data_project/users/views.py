

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.authtoken.models import Token as AuthToken

from django.http import HttpRequest
from rest_framework.decorators import api_view

# curl -X POST -H "Content-Type: application/json" -d '{"username":"myuser", "password":"mypassword", "email":"user@example.com"}' http://127.0.0.1:8000/register/
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"admin"}' http://127.0.0.1:8000/user-login/
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        token, created = AuthToken.objects.get_or_create(user=user)
        auth_login(request=request, user=user)
        return Response({'message': 'Авторизация прошла успешно', 'token': token.key})
    return Response({'message': 'Неверные учетные данные.'}, status=400)