from django import forms
from django.contrib.auth.models import User
from .models import Aluno, Turma

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
        }

    def clean_password_confirm(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password_confirm')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("As senhas não conferem.")
        return p2

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'nota1', 'nota2', 'nota3', 'nota4', 'nota5', 'nota6']
        labels = {
            'nome': 'Nome do Aluno',
            'nota1': '1º Bimestre',
            'nota2': '2º Bimestre',
            'nota3': '3º Bimestre',
            'nota4': '4º Bimestre',
            'nota5': '5º Bimestre',
            'nota6': '6º Bimestre',
        }
        help_texts = {
            'nota1': 'Use N/A caso nao tenha nota.',
            'nota2': 'Use N/A caso nao tenha nota.',
            'nota3': 'Use N/A caso nao tenha nota.',
            'nota4': 'Use N/A caso nao tenha nota.',
            'nota5': 'Use N/A caso nao tenha nota.',
            'nota6': 'Use N/A caso nao tenha nota.',
        }

class TurmaForm(forms.ModelForm):
    alunos_lista = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Digite o nome dos alunos (um por linha)', 'rows': 5}),
        label="Lista de Alunos",
        required=False,
        help_text="Adicione os alunos agora ou deixe em branco para adicionar depois."
    )

    class Meta:
        model = Turma
        fields = ['nome']
        labels = {
            'nome': 'Nome da Turma',
        }

class CSVUploadForm(forms.Form):
    arquivo_csv = forms.FileField(label="Selecione o arquivo CSV")
