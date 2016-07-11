from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    UserListAPIView,
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^profile/$', UserListAPIView.as_view(), name='users_profile'),
    # url(r'^(?P<username>[\w-]+)/$', UserDetailAPIView.as_view(), name='users_detail'),
    # url(r'^detail/$', UserDetailAPIView.as_view(), name='detail'),
]
