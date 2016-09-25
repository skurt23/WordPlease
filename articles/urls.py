# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from articles.api import BlogDetailViewSet
from articles.views import HomeView, BlogsView, BlogDetailView, ArticleDetailView, ArticleCreationView

articles=BlogDetailViewSet.as_view({
    'get': 'list'
})

router = DefaultRouter()
router.register('api/1.0/blog/(?P<username>\w+)', BlogDetailViewSet, base_name='api_blogs_detail')



urlpatterns = [
    url(r'^$', HomeView.as_view(), name='article_home'),
    url(r'^new-post$', ArticleCreationView.as_view(), name='article_creation'),
    url(r'^blogs/$', BlogsView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>\w+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'', include(router.urls))
]
