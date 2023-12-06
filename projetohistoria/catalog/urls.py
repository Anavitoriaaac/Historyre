from django.urls import path
from catalog import views
#from django.contrib.auth import views as auth_view
from .views import  Homepage,ana,ai,login_view,logout_view,detalhes_material,detalhes_etapa #trajetoria


urlpatterns = [ #path('',trajetoria,name='trajetoria')]
    
     path('',views.Homepage, name = "homepage"), 
     path('criarconta',views.criarconta, name = "criarconta"),
      path('ana',views.ana, name = "ana"),
      #path('materiais',views.materiais, name='materiais'),
      path('material/<str:idMaterial>/', detalhes_material, name='detalhes_material'),
      path('ai',views.ai, name = "ai"),
      path('login/', login_view, name='login_view'),
      path('logout/', logout_view, name='logout_view'),
      
      path('etapa/<str:IdEtapa>/', detalhes_etapa, name='detalhes_etapa'),
]



