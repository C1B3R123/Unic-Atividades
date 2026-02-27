# Exercício 5: Tabuada (com intervalo customizável)
numero = int(input("Digite um número para ver sua tabuada: "))
intervalo = int(input("Até qual número deseja calcular a tabuada? (Padrão: 10) ") or 10)

print(f"\n--- Tabuada do {numero} ---")
for i in range(1, intervalo + 1):
    print(f"{numero} x {i} = {numero * i}")