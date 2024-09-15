import os

os.system("cls || clear") #Limpa o terminal.



# Função para somar dois números
def soma(a, b):
    return a + b

# Função para subtrair dois números
def subtracao(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicacao(a, b):
    return a * b

# Função para dividir dois números
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Função principal da calculadora
def calculadora():
    print("Bem-vindo à Mini Calculadora!")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Escolher a operação
    opcao = int(input("Digite o número da operação desejada (1/2/3/4): "))

    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Executar a operação escolhida
    if opcao == 1:
        print(f"Resultado: {soma(num1, num2)}")
    elif opcao == 2:
        print(f"Resultado: {subtracao(num1, num2)}")
    elif opcao == 3:
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == 4:
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida!")

# Chamar a função da calculadora
calculadora()

