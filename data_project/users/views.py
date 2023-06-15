from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer
from django.contrib.auth import authenticate, login as auth_login

from django.http import HttpRequest
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        auth_login(request=request, user=user)
        return Response({'message': 'Аутентификация прошла успешно.'})
    return Response({'message': 'Неверные учетные данные.'}, status=400)