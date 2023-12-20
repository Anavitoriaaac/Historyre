from django.shortcuts import redirect, render, reverse
from.models import Material,Trajetoria,Etapa
from django.contrib import messages
from .forms import MeuFormularioDeLogin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404
from .forms import MaterialForm


def Homepage(request): # representa a view associada à página inicial do site
    #O parâmetro request é um objeto que contém informações sobre a solicitação HTTP recebida
    
    return render (request,'homepage.html') #render ele rederiza paginas html
#recebe request e a pagina html que no caso é o template aser renderizado
# quando alguém acessa a URL associada a esta view (url homepage), o Django chama a função Homepage que renderiza a página HTML 'homepage.html' e a retorna como resposta à solicitação.

def criarconta(request):
    return render (request,'criarconta.html')


def logout_view (request):
    return render(request, 'logout.html')  



def detalhes_etapa(request, IdEtapa): # define o nome da função que mostra os detalhes das etapas 
   #ela aceita dois parâmetros. request O outro IdEtapa, é um parâmetro que espera receber o identificador de uma etapa específica 
   etapa = get_object_or_404(Etapa, IdEtapa= IdEtapa) # Usa a função get_object_or_404 do Django para obter uma instância do modelo Etapa com base no valor de IdEtapa. Se a etapa não for encontrada, retorna uma página 404.
   materiais_da_etapa = etapa.IdMaterial.all() #lista todos os materiais associados à etapa tenho  uma relação muitos para muitos entre Etapa e Material.
   trajetoria_da_etapa = etapa.trajetoria # Obtém a trajetória associada à etapa tenho uma relação ForeignKey entre Etapa e Trajetoria.
   
   return render(request, 'detalhes_etapa.html', {'etapa': etapa, 'trajetoria_da_etapa': trajetoria_da_etapa,'materiais_da_etapa':materiais_da_etapa})
#Retorna uma resposta renderizando o template 'detalhes_etapa.html' e passando um contexto(tipo um dicionario) que inclui a etapa, a trajetoria_da_etapa e os materiais_da_etapa. Essas informações  estao disponiveis e foram usadas na construção da pagina de conteudo.

def conteudo(request):
    
    return render (request,'conteudo.html')











 


def cadastrar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')  # redirecione para a página inicial ou outra página desejada
    else:
        form = MaterialForm()

    return render(request, 'cadastrar_material.html', {'form': form})

def login_view(request):
    # ele vai verifica se a requisição é do tipo postt, indicando que o formulário foi enviado.
    if request.method == 'POST':
        # craia uma instância do formulário de login (MeuFormularioDeLogin) com os dados da requisição post.
        form = MeuFormularioDeLogin(request, data=request.POST)
        # confere se o formulário é válido.
        if form.is_valid():
            # obtem o nome de usuário (username) e a senha (password) do formulário.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # autentica o usuário usando as credenciais fornecidas.
            user = authenticate(username=username, password=password)
            
            # verifica se o usuário é autenticado com sucesso.
            if user is not None:
                # faz o login do usuario na sessao.
                login(request, user)
                # redireciona o usuário para a página 'conteudo' depos d o login.
                return redirect('conteudo')
            else:
                # se as user e senha  sao inválidas exibe uma mensagem de erro.
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            # se o formulário nao for valido  exibe uma mensagem de erro.
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        # se a requisição não for do tipo POST, cria uma instância vazia do formulário de login.
        form = MeuFormularioDeLogin()

    # renderiza a página login.html com o formulário seja ele vazio ou preenchido.
    return render(request, 'login.html', {'form': form})
