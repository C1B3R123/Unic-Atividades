# EduGerente - Sistema de Gestão Escolar

Um sistema simples e seguro desenvolvido em Django para que professores possam gerenciar suas turmas e alunos.

## 🚀 Funcionalidades

- **Landing Page:** Apresentação do sistema.
- **Autenticação Segura:** Login e Registro em página única com navegação por âncoras.
- **Dashboard do Professor:** Visualização de turmas em formato de cards.
- **Gestão de Alunos:** Detalhes da turma, listagem de alunos e visualização de notas.
- **Edição de Dados:** Possibilidade de alterar nomes e notas de alunos.
- **Perfil do Usuário:** Atualização de dados cadastrais do professor.
- **Lista de Docentes:** Visualização de todos os professores cadastrados.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django 6.0**
- **Bootstrap 5** (via `django-bootstrap5`)
- **SQLite3** (Banco de dados padrão)

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

## 🔧 Instalação e Execução

1. **Clone o repositório ou acesse a pasta do projeto:**
   ```bash
   cd SistemaEscolar
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

O sistema estará disponível em: `http://127.0.0.1:8000`

## 🔑 Acesso Inicial

Para testar o sistema, você pode usar a conta de administrador pré-criada:

- **Usuário:** `admin`
- **Senha:** `adminpassword123`

Você pode acessar o painel administrativo em: `http://127.0.0.1:8000/admin/`

## 📂 Estrutura do Projeto

- `config/`: Configurações principais do Django.
- `core/`: Aplicativo principal com modelos, views e lógica do sistema.
- `templates/`: Templates globais (base layout).
- `core/templates/core/`: Templates específicos do aplicativo.

---
Desenvolvido como parte do projeto Unic-Atividades.
