from django.shortcuts import redirect, render, reverse
from.models import Material,Trajetoria,Etapa
from django.contrib import messages
from .forms import MeuFormularioDeLogin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#from .forms import CriarContaForm, FormHomePage
#from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
#from django.contrib.auth.mixins import LoginRequiredMixin



def Homepage(request):
    
    return render (request,'homepage.html')
#def login(request):
  #  return render (request,'login.html')
def criarconta(request):
    return render (request,'criarconta.html')
def ana(request):
    return render (request,'traj.html')
    
#def materiais(request):
  #  materiais= Material.objects.all()
   # return render (request,'material.html', {'materiais': materiais})


from django.shortcuts import render, get_object_or_404


#def materiais(request):
   # materiais = Material.objects.all()
   # return render(request, 'material.html', {'materiais': materiais})

def detalhes_material(request, idMaterial):
    material = get_object_or_404(Material, idMaterial= idMaterial)
    return render(request, 'detalhes_material.html', {'material': material})
def detalhes_etapa(request, IdEtapa):
   etapa = get_object_or_404(Etapa, IdEtapa= IdEtapa)
   materiais_da_etapa = etapa.IdMaterial.all()
   trajetoria_da_etapa = etapa.trajetoria # Se o campo for uma ForeignKey
   
   return render(request, 'detalhes_etapa.html', {'etapa': etapa, 'trajetoria_da_etapa': trajetoria_da_etapa,'materiais_da_etapa':materiais_da_etapa})








def ai(request):
    
    return render (request,'ai.html')


def login_view(request):
    if request.method == 'POST':
        form = MeuFormularioDeLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ai')  # quando faz login redireciona para a pagina da trajetoria
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = MeuFormularioDeLogin()

    return render(request, 'login.html', {'form': form})




from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')  #   URL desejada após o logout (inicio)



