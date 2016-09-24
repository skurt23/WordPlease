from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from articles.views import ArticleQueryset
from users.serializers import UserBlogListSerializer


class BlogListViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('username',)
    order_fields = 'username'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return ArticleQueryset.get_articles_by_user(self.request.user, self.request.user.username)

    def get_serializer_class(self):
        return UserBlogListSerializer
