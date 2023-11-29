from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCAD, null=True, blank=True)

class Comments(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)



