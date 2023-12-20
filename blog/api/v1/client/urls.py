from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.v1.client.views import (UserViewSet, ArticleViewSet,
                                 ArticleManageViewSet, CommentsViewSet, CategoryViewSet,
                                 ArticleOnlyPublishedViewSet, CommentsManageViewSet, CategoryManageViewSet)


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'articles', ArticleViewSet, basename="articles")
router.register(r'articles_manage', ArticleManageViewSet)
router.register(r'articles_only_published', ArticleOnlyPublishedViewSet, basename="articles")
router.register(r'comments', CommentsViewSet, basename='comment')
router.register(r'comments_manage', CommentsManageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'categories_manage', CategoryManageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
