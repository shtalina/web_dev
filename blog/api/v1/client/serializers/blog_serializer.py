from rest_framework import serializers
from main.models import Article, Comments, Category, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']
class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ['id', 'text', 'created_at', 'user', 'article']
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'created_at', 'category', 'published','comments']


class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, source='article_set')
    article_count = serializers.IntegerField(source='count')

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description', 'article_count', 'articles']
