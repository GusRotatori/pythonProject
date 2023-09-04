# Jogo de adivinhação em Python

import random

# Gerar um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Pedir para o jogador adivinhar o número
palpite = int(input("Adivinhe um número entre 1 e 10: "))

# Comparar o palpite do jogador com o número secreto
while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
    palpite = int(input("Tente novamente: "))

# Se o palpite estiver correto, exibir uma mensagem de parabéns
print("Parabéns! Você adivinhou o número!")
