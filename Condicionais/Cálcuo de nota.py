import os

os.system("cls || clear") #Limpa o terminal.

# Entrada
primeira_nota = float(input("Digite a nota da primeira unidade: "))
segunda_nota = float(input("Digite a nota da primeira unidade: "))
terceira_nota = float(input("Digite a nota da primeira unidade: "))

# Processamento
calculo = primeira_nota + segunda_nota + terceira_nota 
media = calculo / 3

if media >= 5:
    resultado = "Você foi aprovado!"
elif media == 4:
    resultado = "Você está no conselho de classe" 
else:
    reultado = "Você está na recuparação"




# Saída
print(resultado)
