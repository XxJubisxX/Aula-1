import os

os.system("cls || clear") #Limpa o terminal.

nome:str = input("Digite seu nome:")
idade:int =input("Digite a sua idade:")
peso:float = input("Digite o seu peso:")


print('Seu nome é {} tem {} anos e pesa {}kg'.format(nome, idade, peso))