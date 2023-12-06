from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.v1.client.views import UserViewSet, ArticleViewSet, CommentsViewSet, CategoryViewSet, TagsViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentsViewSet, basename='comment')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
