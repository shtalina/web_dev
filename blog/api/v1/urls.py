from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = [
    path('client/', include("api.v1.client.urls")),
    path('api-token-auth/', views.obtain_auth_token)
]