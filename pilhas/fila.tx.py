import os

os.system("cls || clear") 

fila = []

while True:
    print('''\nMenu de opções
          1 - Adicionar um elemento a fila
          2 - Visualizar elementos da fila
          3 - Remover o elemento do topo da fila
          4 - Sair do programa''')
    x = int(input('Digite a ação tomada: \n'))
    print('\n')
    match (x):
        case 1:
            y = input('\n Digite o elemento que deseja adicionar a fila: ')
            fila.append(y)
        case 2 :
            if fila == [] :
                print('A fila está vazia: \n')
            for elementos in fila:
                print(elementos)
        case 3:
                fila.pop(0)
        case 4:
            print('Programa encerrado...')
            break
        case _:
            print('comando invalido')