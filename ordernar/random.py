#import os
import random

#os.system("cls || clear") #Limpa o terminal.

atrizes = ["Adrian Prado", "Bárbara Borges", "Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi", "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]

# Embaralha elementos random.shuffle(atrizes)
random.shuffle(atrizes)
print(atrizes)
# Ordena elementos crescentimente
atrizes.sort()# mesmo que usar atrizes.sort(reverse=False)
print(atrizes)
# Ordena elementos decrescentemente
atrizes.sort(reverse = True)
print(atrizes)