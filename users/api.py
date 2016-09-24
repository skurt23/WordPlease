from rest_framework import filters
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework import viewsets, mixins

from articles.views import ArticleQueryset
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer, UserBlogListSerializer


class UserViewSet(viewsets.ViewSet):
    """
    Endpoint de listado de usuarios.

    Para crear un usuario tienes que mandar un JSON que contenga las siguientes propiedades:

    - first_name
    - last_name
    - username
    - password
    - email

    """
    permission_classes = (UserPermission,)

    def list(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class BlogViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
        Endpoint de listado de blogs.

        En este endpoint sólo se listan los blogs, por lo tanto, sólo se admiten peticiones GET. Puedes filtar los
        resultados por nombre de usuario o ordenarlos por id o por nombre de usuario

    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('username',)
    order_fields = 'username'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserBlogListSerializer

