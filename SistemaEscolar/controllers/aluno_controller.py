from database.conexao import get_conexao
from models.aluno import Aluno


class AlunoController:
    @staticmethod
    def cadastrar(aluno):
        conn = get_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO alunos (nome, matricula, curso) VALUES (?, ?, ?)",
                           (aluno.nome, aluno.matricula, aluno.curso))
            conn.commit()
            print("\n[!] Aluno cadastrado com sucesso!")
        except Exception as e:
            print(f"\n[X] Erro ao cadastrar (Matrícula já existe?): {e}")
        finally:
            conn.close()

    @staticmethod
    def listar():
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, matricula, curso FROM alunos")
        linhas = cursor.fetchall()
        conn.close()

        alunos = []
        for linha in linhas:
            alunos.append(
                Aluno(id=linha[0], nome=linha[1], matricula=linha[2], curso=linha[3]))
        return alunos

    @staticmethod
    def atualizar(id_aluno, nome, matricula, curso):
        conn = get_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE alunos 
                SET nome = ?, matricula = ?, curso = ? 
                WHERE id = ?
            """, (nome, matricula, curso, id_aluno))
            conn.commit()

            if cursor.rowcount > 0:
                print("\n[!] Aluno atualizado com sucesso!")
            else:
                print("\n[X] Erro: Nenhum aluno encontrado com esse ID.")
        except Exception as e:
            print(f"\n[X] Erro ao atualizar: {e}")
        finally:
            conn.close()

    @staticmethod
    def deletar(id_aluno):
        conn = get_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
            conn.commit()

            if cursor.rowcount > 0:
                print("\n[!] Aluno deletado com sucesso!")
            else:
                print("\n[X] Erro: Nenhum aluno encontrado com esse ID.")
        except Exception as e:
            print(f"\n[X] Erro ao deletar: {e}")
        finally:
            conn.close()
