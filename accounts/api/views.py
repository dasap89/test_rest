from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

# from .permissions import IsOwnerOrReadOnly
# from posts.models import Post
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
    UserListSerializer,
    )

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, ** kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

class UserListAPIView(ListAPIView):
    # queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = User.objects.all()
    #     # query = self.request.GET.get("q")
    #     query = self.request.user
    #     if query:
		  #  queryset_list = queryset_list.filter(username__icontains=query)
    #     return queryset_list
    def get_queryset(self, *args, **kwargs):
        query = self.request.user
        get_user = User.objects.filter(username__icontains=query)
        return get_user
