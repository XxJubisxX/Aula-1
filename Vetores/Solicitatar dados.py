import os

os.system("cls || clear") #Limpa o terminal.


# Solicitar dados para usuário.


# Exibir os dados.



vetor_notas = []
for i in range(3):
    nota = float(input("Digite uma notas; "))
    vetor_notas.append(nota)

# For Each
for cada_nota in vetor_notas:
    print(cada_nota)    