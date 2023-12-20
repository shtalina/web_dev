from django.contrib import admin
from .models import (
    Article,
    Comments,
    Category,
)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ['category']
    search_fields = ["title", 'text']


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
