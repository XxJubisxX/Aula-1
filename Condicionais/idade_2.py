import os

os.system("cls || clear") #Limpa o terminal.
resposta = ""

# Entrada 
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

# Processamento
if idade >= 65:
    resposta = "Aposentado"
elif idade >= 18:
    resposta = "Maior de idade"
else:
    resposta = "Menor de idade"

# Saída
print(f"Seu nome é: {nome} e você é {resposta}")
print("===== FIM =====")
