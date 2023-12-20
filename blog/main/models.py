from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField()
    count=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.pk} - {self.category_name}'

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} - {self.title}'

class Comments(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.article}'

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
