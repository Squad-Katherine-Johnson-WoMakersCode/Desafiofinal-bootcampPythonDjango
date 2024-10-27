from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User
from time import sleep

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/area_do_autor')
    return render(request, 'login.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/area_do_autor')
    return render(request, 'cadastro.html')

def valida_cadastro(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.WARNING, "Nome ou e-mail não foram preenchidos")
        return redirect('/auth/cadastro/')
    
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, "A senha possui menos de 8 caracateres.")
        return redirect('/auth/cadastro/')
        
    if User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, "E-mail já cadastrado no sistema.")
        return redirect('/auth/cadastro/')
    
    if User.objects.filter(username = nome).exists():
        messages.add_message(request, constants.ERROR, "Nome de usuário já cadastrado no sistema.")
        return redirect('/auth/cadastro/')
    
    try:
        
        usuario = User.objects.create_user(username = nome, email = email, password = senha)
        usuario.save()
        
        messages.add_message(request, constants.SUCCESS, "Cadastro realizado com sucesso!")
        sleep(2)
        return redirect('/auth/login/')
    
    except:
        messages.add_message(request, constants.ERROR, "Erro interno do sistema")
        return redirect('/auth/cadastro/')
    
def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    usuario = auth.authenticate(request,username = nome, password = senha)
    if not usuario:
        messages.add_message(request, constants.WARNING, 'Nome ou senha inválido.')
        return redirect('/auth/login/')
    
    else:
        auth.login(request, usuario)
        request.session['logado'] = True
        return redirect('/plataforma/area_do_autor')
    
def logout(request):
    auth.logout(request)
    return redirect('/news')