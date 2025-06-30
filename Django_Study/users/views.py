from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

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
