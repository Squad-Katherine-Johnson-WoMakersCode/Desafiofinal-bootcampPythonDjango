from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_feed, name = 'news_feed'),
    path('news_completa/<int:id>/', views.news_completa, name='news_completa'),
    path('buscar/', views.buscar_noticias, name='buscar_noticias'),
    path('news_completa/<int:noticia_id>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
]