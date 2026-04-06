# Exercício 8: Jogo de adivinhação
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Bem-vindo ao Jogo de Adivinhação! Pensei em um número entre 1 e 100.")

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        acertou = True
    elif palpite < numero_secreto:
        print("Dica: O número secreto é MAIOR.")
    else:
        print("Dica: O número secreto é MENOR.")