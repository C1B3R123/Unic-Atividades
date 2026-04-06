# 🏫 Sistema Escolar - CRUD MVC

Este é um sistema de gestão escolar simples desenvolvido em **Python**, utilizando o padrão de arquitetura **MVC** (Model-View-Controller) e banco de dados **SQLite**.

O projeto permite o gerenciamento completo (CRUD) de alunos, armazenando os dados localmente em um arquivo `.db`.

## 📂 Estrutura do Projeto

O projeto está organizado seguindo as melhores práticas de separação de responsabilidades:

SistemaEscolar/
│
├── database/
│   └── conexao.py (Configuração e conexão com SQLite)
├── models/
│   └── aluno.py  (Classe que representa a entidade Aluno)
├── controllers/
│   └── aluno_controller.py (Lógica de negócio e comandos SQL)
├── main.py    (Interface de usuário Básica em CMD com menus de interação com o banco)
└── .gitignore   (Arquivo para evitar subir o banco de dados ".db" ao Git)
