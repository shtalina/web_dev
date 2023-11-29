from django.urls import path, include
from rest_framework import routers
from api.v1.client.views import UserViewSet, ArticleViewSet, CommentsViewSet, CategoryViewSet, TagsViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
