from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogoutView, UserGetView


urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', UserGetView.as_view(), name='user'),
    path('create/', UserCreateView.as_view(), name='signup'),
]