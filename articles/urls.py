
from django.conf.urls import url, include
from articles.views import HomeView, BlogsView, BlogDetailView, ArticleDetailView, ArticleCreationView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='article_home'),
    url(r'^new-post$', ArticleCreationView.as_view(), name='article_creation'),
    url(r'^blogs/$', BlogsView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>\w+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$$', ArticleDetailView.as_view(), name='article_detail'),
]
