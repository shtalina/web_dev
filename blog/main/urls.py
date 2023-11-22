from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.article),
    path('main/<int:id>/', views.article_detail),
]