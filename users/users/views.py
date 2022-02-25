from urllib import response
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
import json
from rest_framework import status
from django.contrib.auth.models import User



class CreateUsers(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid:
            error_values =serializer.errors.values()
            error_keys =serializer.errors.keys()

            return Response({next(iter(error_keys)): next(iter(error_values))} , status=status.HTTP_400_BAD_REQUEST)

        try:
            response = User.objects.create_user(**data)
        except Exception as e:
            return Response({"error": ["Error when try create user"]},status=status.HTTP_400_BAD_REQUEST)

        return Response(RegisterSerializer(data=response).data,status=status.HTTP_201_CREATED)


class GetUser(APIView):
    def get(self, request):
        try:
            userList =User.objects.values()
        except:
            return Response({"error": ["Error when try get users"]},status=status.HTTP_400_BAD_REQUEST)
        return Response({'users': [UserSerializer(user).data for user in userList]},status=status.HTTP_200_OK)
