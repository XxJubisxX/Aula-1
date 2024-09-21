import os

os.system("cls || clear") #Limpa o terminal.

# Funções.
def calcular_soma(A, B):
    soma = A + B
    return soma

def calcular_subtracao(A, B):
    subtracao = A - B
    return subtracao

def calcular_smultiplicacao(A, B):
    multiplicacao = A * B
    return multiplicacao

# Entrada.
primeiro_numero = int(input("Digite o primeiro Número: "))
segundo_numero = int(input("Digite o segundo Número: "))



# Processamento.
soma = calcular_soma(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
multiplicacao = calcular_subtracao(primeiro_numero, segundo_numero)


# Saída.
print(f"Soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")

    