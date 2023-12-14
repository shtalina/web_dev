from django_filters.rest_framework import DjangoFilterBackend
from api.v1.client.serializers.blog_serializer import UserSerializer, ArticleSerializer, CommentsSerializer, CategorySerializer
from rest_framework import viewsets, mixins
from main.models import User, Article, Comments, Category

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']

class ArticleOnlyPublishedViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):

    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)
        if article_id is not None:
            return Comments.objects.filter(article=article_id)
        else:
            return Comments.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

