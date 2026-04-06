# Exercício 6: Contador de vogais
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
total_vogais = 0
contagem_separada = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
    if letra in vogais:
        total_vogais += 1
        contagem_separada[letra] += 1

print(f"Total de vogais encontradas: {total_vogais}")
print("Contagem por vogal:")
for vogal, qtd in contagem_separada.items():
    print(f"'{vogal}': {qtd}")