import os

os.system("cls || clear") #Limpa o terminal.

lista = []

while True:
    print("""\nMenu de opções
1 - Adicionar um elemento a lista
2 - Ver a lista de elementos
3 - Remover um elemento da lista
4 - Sair do programa""")

   
    funcao_escolhida = int(input("Digite a ação tomada: \n"))
    print("\n")
    if funcao_escolhida == 1:
        y = input("\nDigite o elemento que deseja adicionar na lista: ")
        lista.append(y)
    elif funcao_escolhida == 2:
        if lista == []:
         print("A lista de elementos está vazia\n")
        for elementos in lista:
         print(elementos)
    elif funcao_escolhida == 3:
        A = 1
        for elementos in lista:
         print(f"{A} - {elementos}")
         A += 1
        y = int(input("\nDigite o número do elemento acima que deseja remover"))
        lista.pop((y-1))
    elif funcao_escolhida == 4:
        print("Programa encerrado...")
        break
    else:
       print("Erro")