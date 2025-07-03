from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.authentication import TokenAuthentication # 사용자 인증 (추가)
from rest_framework.permissions import IsAuthenticated # 권한 부여 (추가)
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

# Create your views here.
class Users(APIView):
    def post(self, request):
        #password=> 검증, 해쉬화해서 저장
        password=request.data.get('password')
        serializer=MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")

        if serializer.is_valid():
            user=serializer.save()
            user.set_password(password)     # 암호화된 해시로 변경
            user.save()

            serializer=MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

class MyInfo(APIView):
    # authentication_classes = [TokenAuthentication]  # 추가
    permission_classes = [IsAuthenticated]  # 추가

    def get(selfself,request):
        user=request.user
        serializer=MyInfoUserSerializer(user)
        return Response(serializer.data)

    def put(self,request):
        user=request.user
        serializer=MyInfoUserSerializer(user,data=request.data,
                                        partial=True)   # 일부 데이터만 담아도 변경을 허용
        if serializer.is_valid():
            user=serializer.save()
            serializer=MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise Response(serializer.errors)

class Login(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        if not username or not password:
            raise ParseError()

        user=authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print("header :",request.headers)
        logout(request)
        return Response(status=status.HTTP_200_OK)

import jwt
from django.conf import settings
class JWTLogin(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        if not username or not password:
            raise ParseError()

        user=authenticate(request, username=username, password=password)

        if user:
            payload={"id":user.id,"username":user.username}
            token=jwt.encode(
                payload,settings.SECRET_KEY, algorithm='HS256'
            )
            return Response({"token",token})

from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        return Response({"id":user.id, "username":user.username})



