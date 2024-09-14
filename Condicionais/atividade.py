import os

os.system("cls || clear") #Limpa o terminal.



# Entrada
t = str(input("Escolha uma operação: Soma:+ Subtração:- Multiplicação:* Divisão:/: "))
n1 = float(input("Digite um número:")) 
n2 = float(input("Digite outro número: ")) 

# Processamento
if t == "+":
    resposta = "Você escolheu Soma"
    resultado = n1 + n2

elif t == "-":
    resposta = "Você escolheu a Subtração"
    resultado = n1 - n2
elif t == "*":
    resposta = "Você escolheu Multiplicação"
    resultado = n1 * n2
elif t == "/":
    resposta = "Você escolheu Divisão"
    resultado = n1 / n2
else:
    resposta = "Operação invlida!!!"


# Saída
print(f"{resposta} e o resultado da operação escolhida é: {resultado}")
