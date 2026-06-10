import csv
import io
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Turma, Aluno
from .forms import UserRegistrationForm, UserProfileForm, AlunoForm, TurmaForm, CSVUploadForm

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

from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Turma, Aluno, Perfil, Materia

def is_diretor(user):
    return hasattr(user, 'perfil') and user.perfil.tipo == 'DIRETOR'

def is_professor(user):
    return hasattr(user, 'perfil') and user.perfil.tipo == 'PROFESSOR'

def is_aprovado(user):
    return hasattr(user, 'perfil') and user.perfil.aprovado

@login_required
def dashboard(request):
    perfil = request.user.perfil
    
    if perfil.tipo == 'DIRETOR':
        # Diretor vê resumo e links de gestão
        pendentes = Perfil.objects.filter(tipo='PROFESSOR', aprovado=False).count()
        return render(request, 'core/dashboard_diretor.html', {'pendentes': pendentes})
        
    elif perfil.tipo == 'PROFESSOR':
        if not perfil.aprovado:
            return render(request, 'core/aguardando_aprovacao.html')
        turmas = Turma.objects.filter(professor=request.user)
        materias = Materia.objects.filter(professor=request.user)
        return render(request, 'core/dashboard_professor.html', {'turmas': turmas, 'materias': materias})
        
    elif perfil.tipo == 'ALUNO':
        aluno = getattr(request.user, 'aluno_profile', None)
        if not aluno:
            return render(request, 'core/erro_aluno.html')
        # Aluno vê suas matérias e notas
        materias = Materia.objects.filter(turma=aluno.turma)
        return render(request, 'core/dashboard_aluno.html', {'aluno': aluno, 'materias': materias})

@login_required
@user_passes_test(is_diretor)
def aprovar_professores(request):
    professores_pendentes = Perfil.objects.filter(tipo='PROFESSOR', aprovado=False)
    if request.method == 'POST':
        perfil_id = request.POST.get('perfil_id')
        acao = request.POST.get('acao')
        perfil_p = get_object_or_404(Perfil, id=perfil_id)
        if acao == 'aprovar':
            perfil_p.aprovado = True
            perfil_p.save()
            messages.success(request, f"Professor {perfil_p.user.username} aprovado!")
        elif acao == 'recusar':
            # Poderia deletar o usuário ou apenas manter desativado
            messages.warning(request, f"Professor {perfil_p.user.username} recusado.")
        return redirect('aprovar_professores')
    return render(request, 'core/aprovar_professores.html', {'pendentes': professores_pendentes})

@login_required
@user_passes_test(is_professor)
def gerenciar_materias(request):
    if not is_aprovado(request.user):
        return redirect('dashboard')
    materias = Materia.objects.filter(professor=request.user)
    turmas = Turma.objects.filter(professor=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        turma_id = request.POST.get('turma_id')
        turma = get_object_or_404(Turma, id=turma_id, professor=request.user)
        Materia.objects.create(nome=nome, professor=request.user, turma=turma)
        messages.success(request, "Materia criada com sucesso!")
        return redirect('gerenciar_materias')
    return render(request, 'core/gerenciar_materias.html', {'materias': materias, 'turmas': turmas})

@login_required
def adicionar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.professor = request.user
            turma.save()
            
            # Processar lista de alunos
            alunos_raw = form.cleaned_data.get('alunos_lista')
            if alunos_raw:
                nomes = [n.strip() for n in alunos_raw.split('\n') if n.strip()]
                for nome in nomes:
                    Aluno.objects.create(nome=nome, turma=turma)
            
            return redirect('dashboard')
    else:
        form = TurmaForm()
    return render(request, 'core/adicionar_turma.html', {'form': form})

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

@login_required
def editar_turma(request, id):
    turma = get_object_or_404(Turma, id=id, professor=request.user)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            turma = form.save()
            
            # Processar lista de alunos (opcional na edição)
            alunos_raw = form.cleaned_data.get('alunos_lista')
            if alunos_raw:
                nomes = [n.strip() for n in alunos_raw.split('\n') if n.strip()]
                for nome in nomes:
                    Aluno.objects.create(nome=nome, turma=turma)
            
            messages.success(request, "Turma atualizada com sucesso!")
            return redirect('turma_detalhe', id=turma.id)
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'core/adicionar_turma.html', {'form': form, 'editando': True, 'turma': turma})

@login_required
def exportar_turma(request, id):
    turma = get_object_or_404(Turma, id=id, professor=request.user)
    alunos = turma.alunos.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="relatorio_{turma.nome}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Nome do Aluno', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nota 6', 'Media Final'])
    
    for aluno in alunos:
        writer.writerow([aluno.nome, aluno.nota1, aluno.nota2, aluno.nota3, aluno.nota4, aluno.nota5, aluno.nota6, aluno.nota_media])
        
    return response

@login_required
def importar_alunos(request, id):
    turma = get_object_or_404(Turma, id=id, professor=request.user)
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['arquivo_csv']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV.")
                return redirect('turma_detalhe', id=id)
            
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string) # Pular cabecalho
            
            count = 0
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                if len(row) >= 1:
                    nome = row[0]
                    # Pegar notas se existirem, senao usar N/A
                    n1 = row[1] if len(row) > 1 else "N/A"
                    n2 = row[2] if len(row) > 2 else "N/A"
                    n3 = row[3] if len(row) > 3 else "N/A"
                    n4 = row[4] if len(row) > 4 else "N/A"
                    n5 = row[5] if len(row) > 5 else "N/A"
                    n6 = row[6] if len(row) > 6 else "N/A"
                    
                    Aluno.objects.create(
                        nome=nome, 
                        nota1=n1, nota2=n2, nota3=n3, 
                        nota4=n4, nota5=n5, nota6=n6,
                        turma=turma
                    )
                    count += 1
            
            messages.success(request, f"{count} alunos importados com sucesso!")
            return redirect('turma_detalhe', id=id)
    return redirect('turma_detalhe', id=id)

@login_required
def download_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="template_alunos.csv"'
    
    writer = csv.writer(response)
    # Cabecalhos sem acentos para evitar problemas de encoding
    writer.writerow(['Nome do Aluno', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nota 6'])
    writer.writerow(['Exemplo Aluno 1', '8.5', '7.0', 'N/A', 'N/A', 'N/A', 'N/A'])
    writer.writerow(['Exemplo Aluno 2', '6.0', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'])
    
    return response
