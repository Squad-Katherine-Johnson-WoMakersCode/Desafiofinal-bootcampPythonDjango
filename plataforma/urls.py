from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('home/criar_artigo/', views.criar_artigo, name='criar_artigo'),
]