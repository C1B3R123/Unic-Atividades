from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acesso/', views.acesso, name='acesso'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('turma/nova/', views.adicionar_turma, name='adicionar_turma'),
    path('turma/<int:id>/', views.turma_detalhe, name='turma_detalhe'),
    path('aluno/<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('perfil/', views.perfil, name='perfil'),
    path('professores/', views.lista_professores, name='lista_professores'),
    path('logout/', views.logout_view, name='logout'),
]
