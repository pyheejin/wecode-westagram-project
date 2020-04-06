from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import JsonResponse

from .models import Comment


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        Comment(
            name=data['name'],
            text=data['text'],
        ).save()
        print(data)
        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        comment = Comment.objects.values()
        return JsonResponse({'comments':list(comment)}, status=200)