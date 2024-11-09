import os

os.system("cls || clear") #Limpa o terminal.

# Cria uma fila com trÊs elementos.
fila =["Banana", "Maçã", "Pera"]
print ("Fila: ", fila)

# Andiciona um elemento ao final da fila.
fila.append("Uva")
print("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado á fila.
fila.pop(0)
print("Removendo um elemento:", fila)
