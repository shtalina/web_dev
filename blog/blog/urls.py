from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User


# Routers provide an easy way of automatically determining the URL conf.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]