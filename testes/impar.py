import os

os.system("cls || clear") #Limpa o terminal.



def verificar(valor):
    if valor % 2 == 0:
        return print(F"O número {valor} é par.")
    else: 
        return print(F"O número {valor} é ímpar.")

numero = int(input("Digite um valor: "))
verificar(numero)