import os

os.system("cls || clear") #Limpa o terminal.

stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Elementos inseridos na stack foram: ')
print(stack)

print('Excluir elementos da stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack.atual:")
print(stack)