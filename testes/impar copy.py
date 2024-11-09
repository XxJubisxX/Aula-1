import os

os.system("cls || clear") #Limpa o terminal.



def valor(x):
    if x > 100:
        valor = x * 0.2
        inflacao = valor + x
    else: 
        valor = x * 0.1
        inflacao = valor + x
        return print(F"O valor da inflação é: {inflacao}")

valor_gasto = int(input("Digite um valor: "))
valor(valor_gasto)