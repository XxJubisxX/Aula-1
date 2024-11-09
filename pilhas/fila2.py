import os

os.system("cls || clear") #Limpa o terminal.


fila = []

# Adicionando elementos na fila a partir da entrada do usuário
for i in range(3):
    num = int(input("Digite um número: "))
    fila.append(num)
print(fila) #Saída: [num1,num2,num3]

# Removendo o elemento mais antigo da fila
primeiro_elemento = fila.pop(0)
print(primeiro_elemento) # Saída: num1
print(fila) # Saída: [num2,num3]