import os

os.system("cls || clear") #Limpa o terminal.


import random

def jogo_adivinhar_numero():
    print("Bem-vindo ao jogo de Adivinhação!")
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")

    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        # Entrada do jogador
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        # Verificação do palpite
        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

# Iniciar o jogo
jogo_adivinhar_numero()
