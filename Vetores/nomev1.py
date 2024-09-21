import os

os.system("cls || clear") #Limpa o terminal.


vetor_nomes = []
for i in range(4):
    nome = str(input(f"Digite o{i+1}º nome: "))
    vetor_nomes.append(nome)

for cada_nome in enumerte(vetor_nomes, start=1):
    print(f"Nome: {cada_nome}")    