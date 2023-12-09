from django.urls import path
from catalog import views
#from django.contrib.auth import views as auth_view
from .views import  Homepage,ana,login_view,logout_view,detalhes_etapa,conteudo  #trajetoria


urlpatterns = [ 
    
      path('',views.Homepage, name = "homepage"), # quando a URL for vazia, chama a função homepage da viewsHomepage e atribui o nome 'homepage' a essa URL.
      path('criarconta',views.criarconta, name = "criarconta"), # Quando a URL for 'criarconta', chama a função criarconta da views.criarconta e atribui o nome 'criarconta' a essa URL e  asimm por diante.
      path('ana',views.ana, name = "ana"),

      path('conteudo',views.conteudo, name = "conteudo"),
      path('login/', views.login_view, name='login_view'),
      path('logout/', views.logout_view, name='logout_view'),
      path('etapa/<str:IdEtapa>/', views.detalhes_etapa, name='detalhes_etapa'), 
# define uma URL dinâmica que espera uma string (str) na posição <str:IdEtapa>/, chama a função detalhes_etapa e atribui o nome 'detalhes_etapa' a essa URL.
]



