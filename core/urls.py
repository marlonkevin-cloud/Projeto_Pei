
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("projetos/",views.lista_projetos,name="lista_projetos"),
    path("projetos/criar/",views.criar_projeto,name="criar_projeto"),
    path("projetos/editar/<int:pk>/",views.editar_projeto,name="editar_projeto"),
    path("projetos/excluir/<int:pk>/",views.excluir_projeto,name="excluir_projeto"),
]
