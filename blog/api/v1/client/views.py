from api.v1.client.serializers.blog_serializer import UserSerializer, ArticleSerializer, CommentsSerializer, CategorySerializer, TagsSerializer
from rest_framework import routers, serializers, viewsets
from main.models import User, Article, Comments, Category, Tags


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)
        if article_id is not None:
            return Comments.objects.filter(article=article_id)
        else:
            return Comments.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
