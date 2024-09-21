import os

os.system("cls || clear") #Limpa o terminal.


vetor_nomes = []
for i in range(4):
    nome = str(input("Digite um nome: "))
    vetor_nomes.append(nome)

for cada_nome in vetor_nomes:
    print(cada_nome)    