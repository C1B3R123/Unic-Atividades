from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acesso/', views.acesso, name='acesso'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aprovar-professores/', views.aprovar_professores, name='aprovar_professores'),
    path('materias/', views.gerenciar_materias, name='gerenciar_materias'),
    path('turma/nova/', views.adicionar_turma, name='adicionar_turma'),
    path('turma/<int:id>/', views.turma_detalhe, name='turma_detalhe'),
    path('turma/<int:id>/editar/', views.editar_turma, name='editar_turma'),
    path('turma/<int:id>/exportar/', views.exportar_turma, name='exportar_turma'),
    path('turma/<int:id>/importar/', views.importar_alunos, name='importar_alunos'),
    path('download-template/', views.download_template, name='download_template'),
    path('aluno/<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('perfil/', views.perfil, name='perfil'),
    path('professores/', views.lista_professores, name='professores'),
    path('logout/', views.logout_view, name='logout'),
]
