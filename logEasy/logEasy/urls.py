
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recebimento/', views.produtos_view, name='recebimento'),
    path('estoque/', views.listar_produto, name='listar_produto'),
    path('', views.index, name='index'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('expedicao/', views.listar_P2, name='listar_P2'),
    path('expedicao/saida/<int:produto_id>/', views.processar_saida_estoque, name='dar_saida'),
]