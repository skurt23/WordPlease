from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.api import BlogViewSet

router = DefaultRouter()
router.register('api/1.0/users', UserViewSet, base_name='api_user')
router.register('api/1.0/blogs', BlogViewSet, base_name='api_blogs')
urlpatterns = [
    url(r'', include(router.urls))
]
