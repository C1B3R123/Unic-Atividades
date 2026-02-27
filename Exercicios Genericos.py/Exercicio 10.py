# Exercício 10: Salvar e ler tarefas
import os

ARQUIVO = "tarefas.txt"

while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")
    opcao = input("Opção: ")
    
    if opcao == '1':
        tarefa = input("Digite a nova tarefa: ")
        with open(ARQUIVO, "a", encoding="utf-8") as file:
            file.write(tarefa + "\n")
        print("Tarefa salva com sucesso!")
        
    elif opcao == '2':
        if os.path.exists(ARQUIVO):
            print("\nSujas Tarefas:")
            with open(ARQUIVO, "r", encoding="utf-8") as file:
                linhas = file.readlines()
                for idx, linha in enumerate(linhas, 1):
                    print(f"{idx}. {linha.strip()}")
        else:
            print("\nNenhuma tarefa cadastrada ainda.")
            
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")