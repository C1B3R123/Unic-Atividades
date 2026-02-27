# Exercício 7: Lista de números
n = int(input("Quantos números deseja inserir? "))

while n <= 0:
    print("Quantidade inválida. Digite um valor maior que zero.")
    n = int(input("Quantos números deseja inserir? "))

numeros = []
for i in range(n):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")