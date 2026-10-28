from django.shortcuts import render
from .serializers import CreateUserSerializer, UserLoginSerializer, UserResponseSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny 


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserResponseSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        # serializer returns python dict 
        # {"email": "example@gmail.com", "pass":"secret pass"}
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        return Response(UserResponseSerializer(user).data, status=status.HTTP_200_OK)
