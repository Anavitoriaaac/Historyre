"""
URL configuration for projetohistoria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),  # define a URL para o painel de administração do Django.
    path ('',include('catalog.urls')), # inclui as URLs do aplicativo catalog.
    path('catalog/', include('catalog.urls')), # inclui as URLs do aplicativo catalog sob o prefixo 'catalog/'.
]

# Importa as configurações do Django do arquivo settings.py
from django.conf import settings
# Importa a função static que é usada para adicionar as configurações de rota para servir arquivos estáticos e de mídia.
from django.conf.urls.static import static

# Verifica se o aplicativo está em modo de depuração.
if settings.DEBUG:
    # adiciona as configurações para servir arquivos estáticos.
    # settings.STATIC_URL é o URL prefixo para os arquivos estáticos.
    # settings.STATIC_ROOT é o caminho absoluto para o diretório onde esses arquivos estão armazenados.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # adiciona as configurações para servir arquivos de mídia.
    # settings.MEDIA_URL é o URL prefixo para os arquivos de mídia.
    # settings.MEDIA_ROOT é o caminho absoluto para o diretório onde esses arquivos estão armazenados.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
