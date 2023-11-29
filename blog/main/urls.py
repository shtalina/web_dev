from django.urls import path
from . import views

urlpatterns = [
    path('api/', include('api.urls'))
]
