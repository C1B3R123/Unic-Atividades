# Exercício 9: Calculadora simples
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

while True:
    print("\n--- Calculadora ---")
    print("1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir | 0. Sair")
    escolha = input("Escolha a operação: ")
    
    if escolha == '0':
        break
    if escolha in ['1', '2', '3', '4']:
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        
        if escolha == '1': print(f"Resultado: {somar(x, y)}")
        elif escolha == '2': print(f"Resultado: {subtrair(x, y)}")
        elif escolha == '3': print(f"Resultado: {multiplicar(x, y)}")
        elif escolha == '4': print(f"Resultado: {dividir(x, y)}")
    else:
        print("Opção inválida.")