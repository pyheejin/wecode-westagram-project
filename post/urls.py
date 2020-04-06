from django.urls import path
from .views import CommentView, myCommentView

urlpatterns = [
    path('comments/', CommentView.as_view(), name='comment'),
    path('<str:name>/', myCommentView.as_view(), name='mycomment'),
]