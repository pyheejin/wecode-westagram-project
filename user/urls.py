from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogoutView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
    path('create/', UserCreateView.as_view(), name='apis_v1_user_create'),
]