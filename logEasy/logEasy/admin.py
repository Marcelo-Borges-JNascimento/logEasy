from django.contrib import admin
# Importamos as models que estão na mesma pasta
from .models import Departamento, Produtos, HistoricoExpedicao 

# Registramos para aparecerem no painel /admin
admin.site.register(Departamento)
admin.site.register(Produtos)
admin.site.register(HistoricoExpedicao)