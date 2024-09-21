import os

os.system("cls || clear") #Limpa o terminal.

#Função.
quantidade_de_nota = 3

def logo_senai():
    print("======SENAI======")



Lista_de_notas = []
for i in range(3):
    os.system("cls || clear") #Limpa o terminal.
    notas = float(input("Digite uma nota: "))
    Lista_de_notas.append(notas)

for cada_nota in Lista_de_notas:
    print(cada_nota)
    
# Processamento.
def calcular_media(lista_notas):

    soma = sum(Lista_de_notas) # Função com retorno.
    media_calculada = soma / quantidade_de_nota
    return media_calculada

media = calcular_media(Lista_de_notas)

# Saída.

print("As notas digitas foram:", Lista_de_notas)
print("A média é:", media )

