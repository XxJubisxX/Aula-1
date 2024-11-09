import os

os.system("cls || clear") #Limpa o terminal.

item = str(input("O que deseja comprar ?"))
quantidade = int(input("Digite a quantidade desejada: "))

print("Os produtos custam individualmente R$:1,30 e R$:1,00 a dúzia.")

if quantidade > 12:
    valor = 1
    x = valor * quantidade
    print(f"O valor sera R$:{x:.2f}")

else:
    valor = 1.3
    x = valor * quantidade
    print(f"O valor sera R$:{x:.2f}")