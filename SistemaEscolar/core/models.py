from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='turmas', verbose_name="Professor Responsável")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Aluno(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Aluno")
    nota_media = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, verbose_name="Nota Média")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos', verbose_name="Turma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
