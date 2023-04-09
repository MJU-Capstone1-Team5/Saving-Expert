from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "albums"

urlpatterns = [
    path('main', views.main, name='main'),
]