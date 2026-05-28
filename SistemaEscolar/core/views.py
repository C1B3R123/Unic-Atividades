from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Turma, Aluno
from .forms import UserRegistrationForm, UserProfileForm, AlunoForm

def index(request):
    return render(request, 'core/index.html')

def acesso(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    login_form = AuthenticationForm()
    register_form = UserRegistrationForm()
    
    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('dashboard')
        elif 'register_submit' in request.POST:
            register_form = UserRegistrationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('dashboard')
                
    return render(request, 'core/acesso.html', {
        'login_form': login_form,
        'register_form': register_form
    })

@login_required
def dashboard(request):
    turmas = Turma.objects.filter(professor=request.user)
    return render(request, 'core/dashboard.html', {'turmas': turmas})

@login_required
def turma_detalhe(request, id):
    turma = get_object_or_404(Turma, id=id, professor=request.user)
    alunos = turma.alunos.all()
    return render(request, 'core/turma_detalhe.html', {'turma': turma, 'alunos': alunos})

@login_required
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id, turma__professor=request.user)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('turma_detalhe', id=aluno.turma.id)
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'core/editar_aluno.html', {'form': form, 'aluno': aluno})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'core/perfil.html', {'form': form})

@login_required
def lista_professores(request):
    professores = User.objects.all()
    return render(request, 'core/lista_professores.html', {'professores': professores})

def logout_view(request):
    logout(request)
    return redirect('index')
