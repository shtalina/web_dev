from django_filters.rest_framework import DjangoFilterBackend
from api.v1.client.serializers.blog_serializer import UserSerializer, ArticleSerializer, CommentsSerializer, CategorySerializer
from rest_framework import viewsets, mixins, authentication, permissions, status
from rest_framework.response import Response
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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)
        if article_id is not None:
            return Comments.objects.filter(article=article_id)
        else:
            return Comments.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "Comment created successfully"}, status=status.HTTP_201_CREATED)
        # Ваша логика создания комментария
        return Response({"message": "You need to be authenticated to create a comment"},
                            status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        if request.user.is_authenticated:
            return Response({"message": "Comment updated successfully"})
        # Ваша логика обновления комментария
        return Response({"message": "You need to be authenticated to update a comment"}, status=status.HTTP_401_UNAUTHORIZED)


    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"message": "Comment deleted successfully"})
        # Ваша логика удаления комментария
        return Response({"message": "You need to be authenticated to delete a comment"},
                            status=status.HTTP_401_UNAUTHORIZED)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "Category created successfully"}, status=status.HTTP_201_CREATED)
        # Ваша логика создания комментария
        return Response({"message": "You need to be authenticated to create a category"},
                            status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        if request.user.is_authenticated:
            return Response({"message": "Categoryt updated successfully"})
        # Ваша логика обновления комментария
        return Response({"message": "You need to be authenticated to update a Category"}, status=status.HTTP_401_UNAUTHORIZED)


    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"message": "Comment deleted successfully"})
        # Ваша логика удаления комментария
        return Response({"message": "You need to be authenticated to delete a comment"},
                            status=status.HTTP_401_UNAUTHORIZED)

class ArticleManageViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

