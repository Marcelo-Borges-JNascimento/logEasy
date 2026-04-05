
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recebimento/', views.produtos_view, name='recebimento'),
    path('estoque/', views.listar_produto, name='listar_produto'),
    path('', views.index, name='index')
]
