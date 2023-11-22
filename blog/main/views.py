from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article, User, Comments, Category, Tags
from .serializers import ArticleSerializer, CommentsSerializer, CategorySerializer, TagsSerializer, UserSerializer

@csrf_exempt

def article(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        category_s = CategorySerializer()

        articles = Article.objects.all()
        article_s = ArticleSerializer(many=True)

        return JsonResponse(article_s.data, safe=False)

def article_detail(request, id):

    if request.method == 'GET':
        articles = Article.objects.get(pk=id)
        article_s = ArticleSerializer(many=True)

        comments = Comments.objects.filter(id=article)
        comments_s = CommentsSerializer(many=True)

        category = Category.objects.get(id=id)
        category_s = CategorySerializer()

        return JsonResponse(article_s.data, comments_s.data, category_s.data, tag_s.data,  safe=False)




