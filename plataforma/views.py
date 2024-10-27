from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q

@login_required(login_url = '/auth/login')
def area_do_autor(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'area_do_autor.html', {'noticias': noticias})

def criar_artigo(request):
    return render (request, 'criar_artigo.html')

def criar_artigo(request):
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        conteudo = request.POST.get('conteudo')
        imagem = request.FILES.get('imagem')
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        
        noticia = Noticia.objects.create(
            titulo=titulo, subtitulo=subtitulo, conteudo=conteudo, imagem=imagem, categoria=categoria, autor=request.user
        )
        
        return redirect('area_do_autor')
    
    categorias = Categoria.objects.all()
    return render(request, 'criar_artigo.html', {'categorias': categorias})

def excluir_noticia(request, id):
    if request.method == 'POST':
        noticia = get_object_or_404(Noticia, id=id)
        noticia.delete()
        messages.add_message(request, constants.SUCCESS, "Notícia excluída com sucesso.")
        return redirect('area_do_autor')
    else:
        messages.add_message(request, constants.ERROR, "Você não tem permissão para excluir uma notícia.")
        return redirect('area_do_autor')

def buscar_noticias(request):
    query = request.GET.get('q')  # Palavra-chave
    autor = request.GET.get('autor')  # Autor
    categoria = request.GET.get('categoria')  # Categoria

    noticias = Noticia.objects.all()

    # Filtros dinâmicos
    if query:
        noticias = noticias.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))

    if autor:
        noticias = noticias.filter(autor__icontains=autor)

    if categoria:
        noticias = noticias.filter(categoria__id=categoria)

    categorias = Categoria.objects.all()  

    return render(request, 'noticias.html', {
        'noticias': noticias, 
        'query': query, 
        'autor': autor, 
        'categorias': categorias
    })