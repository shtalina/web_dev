from rest_framework import serializers
from .models import Article, Tags, Comments, Category, User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'created_at', 'category']

class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()

    class Meta:
        model = Comments
        fields = ['id', 'text', 'created_at', 'user', 'article']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag_name']