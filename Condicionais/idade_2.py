import os

os.system("cls || clear") #Limpa o terminal.
resposta = ""

# Entrada
nome = str(input("Digite o seu nome:"))
idade = int(input("Digite sua idade:"))

# Processamento
if idade >= 18:
    resposta = "Maioridade"
elif idade >= 65:
    resposta = "Aposentado"    
else:
    resposta = "Menorde idade"
# Saída
print(f"Seu nome é:{nome} e você é {resposta}")
print("=====FIM====")