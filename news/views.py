from django.shortcuts import render, get_object_or_404, redirect
from plataforma.models import Noticia, Categoria, Comentarios
from django.db.models import Q


def news_feed(request):
    noticias = Noticia.objects.filter(status='PU')
    categorias = Categoria.objects.all()

    return render(request, 'news_feed.html', {'noticias': noticias, 'categorias': categorias})

def news_completa(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    comentarios = noticia.comentarios.all() 
    return render(request, 'news_completa.html', {'noticia': noticia, "comentarios": comentarios})

def buscar_noticias(request):
    query = request.GET.get('q')
    autor = request.GET.get('autor')
    categoria = request.GET.get('categoria')

    noticias = Noticia.objects.filter(status='PU')

    if query:
        noticias = noticias.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))

    if autor:
        noticias = noticias.filter(autor__username__icontains=autor)  

    if categoria:
        noticias = noticias.filter(categoria__id=int(categoria)) 
        
    if not autor and not query and not categoria:
        pass

    categorias = Categoria.objects.all()

    return render(request, 'resultado_busca.html', {
        'noticias': noticias,
        'query': query,
        'autor': autor,
        'categoria': categoria,  
        'categorias': categorias
    })
    
def adicionar_comentario(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        autor = request.POST.get('autor') 
        comentario = request.POST.get('comentario')  

        
        if autor and comentario:
            
            comentario = Comentarios(noticia=noticia, autor=autor, comentario=comentario)
            comentario.save()  
            return redirect('news_completa', id=noticia.id)  
        else:
            error_message = "Todos os campos devem ser preenchidos."
            return render(request, 'news_completa.html', {'noticia': noticia, 'error_message': error_message})

    return render(request, 'news_completa.html', {'noticia': noticia})