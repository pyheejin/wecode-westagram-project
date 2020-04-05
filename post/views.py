from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import JsonResponse

from user.models import User
from .models import Comment


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            name=data['name'],
            text=data['text'],
        ).save()
        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(selfself, request):
        comment = Comment.objects.values()
        return JsonResponse({'users':list(comment)}, status=200)