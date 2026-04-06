import sqlite3
import os


def get_conexao():
    # Cria o arquivo de banco de dados na raiz do projeto (SistemaEscola/escola.db)
    caminho_db = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'escola.db')
    conn = sqlite3.connect(caminho_db)
    return conn


def criar_tabelas():
    conn = get_conexao()
    cursor = conn.cursor()
    # Cria a tabela de alunos se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            curso TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
