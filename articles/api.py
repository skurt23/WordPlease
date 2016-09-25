from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from django.utils import timezone

from articles.permissions import ArticlePermission
from articles.serializers import ArticleListSerializer, ArticleSerializer
from articles.views import ArticleListApiQueryset, ArticleQueryset


class BlogDetailViewSet(ModelViewSet):
    """
    Endpoint de artículos. Un usuario no autenticado sólo podrá ver los artículos publicados

    Para crear un artículo tendrás que estar autenticado y el artículo se publicará inmediatamente en tu blog.

    Si se desea actualizar o eliminar un artículo debe hacerlo el propietario de ese artículo o un administrador
    """
    permission_classes = (IsAuthenticatedOrReadOnly, ArticlePermission)
    search_fields = ('title', 'small_text',)
    order_fields = ('title', 'publication_date', 'categories')
    ordering = ('-publication_date',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return ArticleListApiQueryset.get_articles_by_user(self.request.user, self.kwargs['username'])

    def get_serializer_class(self):
        if self.action != 'list':
            return ArticleSerializer
        else:
            return ArticleListSerializer


    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, publication_date=timezone.now())

    def perform_update(self, serializer):
        user = User.objects.filter(username=self.kwargs['username'])
        return serializer.save(author=user[0], publication_date=timezone.now())








