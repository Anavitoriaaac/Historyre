from django.contrib import admin 
from catalog.models import Etapa,Trajetoria,Material,Usuario,Historico
# Register meus modelos.
admin.site.register(Etapa)
admin.site.register(Trajetoria)
admin.site.register(Material)
admin.site.register(Usuario)
admin.site.register(Historico)