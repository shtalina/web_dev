from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.v1.client.views import UserViewSet, ArticleViewSet, CommentsViewSet, CategoryViewSet, ArticleOnlyPublishedViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'articles', ArticleViewSet, basename="articles")
router.register(r'articles_only_published', ArticleOnlyPublishedViewSet, basename="articles")
router.register(r'comments', CommentsViewSet, basename='comment')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]