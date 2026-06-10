from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    TIPOS = (
        ('DIRETOR', 'Diretor'),
        ('PROFESSOR', 'Professor'),
        ('ALUNO', 'Aluno'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=20, choices=TIPOS, default='PROFESSOR')
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        # Primeiro usuario criado via admin ou shell pode ser diretor/aprovado
        tipo = 'PROFESSOR'
        aprovado = False
        if instance.is_superuser:
            tipo = 'DIRETOR'
            aprovado = True
        Perfil.objects.create(user=instance, tipo=tipo, aprovado=aprovado)

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='turmas', verbose_name="Professor Responsavel")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno_profile', null=True, blank=True)
    nome = models.CharField(max_length=200, verbose_name="Nome do Aluno")
    # ... (notas fields)
    nota1 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 1º Bimestre")
    nota2 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 2º Bimestre")
    nota3 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 3º Bimestre")
    nota4 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 4º Bimestre")
    nota5 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 5º Bimestre")
    nota6 = models.CharField(max_length=5, default="N/A", verbose_name="Nota 6º Bimestre")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos', verbose_name="Turma")

    def __str__(self):
        return self.nome

    @property
    def nota_media(self):
        notas_campos = [self.nota1, self.nota2, self.nota3, self.nota4, self.nota5, self.nota6]
        valid_notas = []
        for nota in notas_campos:
            if nota and str(nota).strip().upper() != "N/A":
                try:
                    val = float(str(nota).replace(',', '.'))
                    valid_notas.append(val)
                except ValueError:
                    continue
        
        if not valid_notas:
            return 0.0
        return round(sum(valid_notas) / len(valid_notas), 2)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materias')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='materias', null=True)

    def __str__(self):
        return f"{self.nome} ({self.turma.nome if self.turma else 'Sem Turma'})"
