from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    
    STATUS_CHOICES = {
        "AN": "Em análise",
        "PU": "Publicado",
    }
         
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    conteudo = models.TextField()
    capa = models.ImageField(upload_to='noticias/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default = 'AN')


    def __str__(self):
        return self.titulo
    
class Comentarios(models.Model):
    
    comentario = models.TextField()
    autor = models.CharField(max_length=100)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario