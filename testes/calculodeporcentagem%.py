import os

os.system("cls || clear") #Limpa o terminal.

#Entrada
valor = float(input("Digite um valor desejado para o desconto de 10%: "))

#Processamento
#cálculo de 10%
x = valor * 0.1 
desconto = valor - x



#Saída
print(f"O valor com desconto será {desconto} ")