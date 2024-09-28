import os

os.system("cls || clear") 
quantidade_de_elementos = 20
lista = [0] * quantidade_de_elementos
while True:
    print("""\nMenu de opções
1 - Empilhar
2 - Listar
3 - Remover um elemento da lista
4 -
5 -
6 - Sair do programa""")
    
    x = int(input("Digite a ação tomada: \n"))
    print("\n")
    if x == 1:
        y = input("\nDigite o livro que deseja adicionar na lista: ")
        lista.append(y)
    elif x == 2:
        if lista == []:
         print("A lista de elementos está vazia\n")
        for elementos in lista:
         print(elementos)
    elif x == 3:
        k = 1
        for elementos in lista:
         print(f"{k} - {livros}")
         k += 1
        y = int(input("\nDigite o número do livro acima que deseja remover"))
        lista.pop((y-1))
    
    
    elif x == 6:
        print("Programa encerrado...")
        break
    else:
       print("Erro")
