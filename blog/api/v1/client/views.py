from django_filters.rest_framework import DjangoFilterBackend
from api.v1.client.serializers.blog_serializer import UserSerializer, ArticleSerializer, CommentsSerializer, CategorySerializer
from rest_framework import viewsets, mixins, authentication, permissions, status
from rest_framework.response import Response
from main.models import User, Article, Comments, Category

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']


class ArticleOnlyPublishedViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet,
    ):
    queryset = Article.objects.filter(published=True).all()
    serializer_class = ArticleSerializer


class CommentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleManageViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CategoryManageViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name', 'article']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CommentsManageViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filterset_fields = ['article', 'created_at']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
