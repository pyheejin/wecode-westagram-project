from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError
from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import User


class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)


class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(email=data['email']).exists():
            user = User.objects.get(email=data['email'])
            if user.password == data['password']:
                return JsonResponse({'message': '로그인 성공'}, status=200)
            else:
                return JsonResponse({'message': '비밀번호를 확인하세요'}, status=200)

        return JsonResponse({'message': '입력 정보를 확인해주세요'}, status=200)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({'message': '로그아웃 성공'}, status=200)


class UserCreateView(BaseView):
    def post(self, request):
        data = json.loads(request.body)
        User(
            name=data['name'],
            email=data['email'],
            password=data['password'],
        ).save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)


class UserGetView(View):
    def get(self, request):
        user_data = User.objects.values()
        return JsonResponse({'users': list(user_data)}, status=200)