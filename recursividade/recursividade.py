import os
import time

os.system("cls || clear")

Numero_escolhido = int(input("Digite um número: "))
N2 = int
resultado = int

def contagem_regressiva(numero):
    if numero < 0:
        return
    print(numero)
    time.sleep(1)
    contagem_regressiva(numero -1)

def soma_contagem(numero):
    if numero == 0:
       return 0
    else:
        print(f"{numero} + {numero}")
      

print("contagem regressiva...")
contagem_regressiva(Numero_escolhido)
soma_contagem(numero=)
print(f"Soma:  {soma_contagem(Numero_escolhido)}")
print("=== FIM ==")


