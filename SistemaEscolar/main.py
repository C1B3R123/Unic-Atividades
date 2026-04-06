from database.conexao import criar_tabelas
from models.aluno import Aluno
from controllers.aluno_controller import AlunoController


def menu():
    print("\n" + "="*30)
    print("      SISTEMA ESCOLAR      ")
    print("="*30)
    print("1 - Cadastrar Novo Aluno   (CREATE)")
    print("2 - Listar Alunos          (READ)")
    print("3 - Atualizar Aluno        (UPDATE)")
    print("4 - Deletar Aluno          (DELETE)")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    # Inicializa o banco de dados
    criar_tabelas()

    while True:
        opcao = menu()

        if opcao == '1':
            print("\n--- CADASTRO DE ALUNO ---")
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            curso = input("Curso: ")

            novo_aluno = Aluno(nome, matricula, curso)
            AlunoController.cadastrar(novo_aluno)

        elif opcao == '2':
            alunos = AlunoController.listar()
            print("\n--- LISTA DE ALUNOS ---")
            if not alunos:
                print("Nenhum aluno cadastrado no momento.")
            for aluno in alunos:
                print(
                    f"ID: {aluno.id} | Nome: {aluno.nome} | Matrícula: {aluno.matricula} | Curso: {aluno.curso}")

        elif opcao == '3':
            print("\n--- ATUALIZAR ALUNO ---")
            id_aluno = input("Digite o ID do aluno que deseja atualizar: ")
            nome = input("Novo nome: ")
            matricula = input("Nova matrícula: ")
            curso = input("Novo curso: ")

            AlunoController.atualizar(id_aluno, nome, matricula, curso)

        elif opcao == '4':
            print("\n--- DELETAR ALUNO ---")
            id_aluno = input("Digite o ID do aluno que deseja deletar: ")
            certeza = input(
                f"Tem certeza que deseja deletar o aluno ID {id_aluno}? (S/N): ").strip().upper()

            if certeza == 'S':
                AlunoController.deletar(id_aluno)
            else:
                print("\n[!] Operação de exclusão cancelada.")

        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente nvamente.")


if __name__ == "__main__":
    main()
