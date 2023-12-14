from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('client/', include("api.v1.client.urls")),    
]