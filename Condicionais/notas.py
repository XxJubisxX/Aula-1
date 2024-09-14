import os

os.system("cls || clear") #Limpa o terminal.

# Entrada.
nota = float(input("Digite uma nota"))

# Processamento.
if nota >= 7:
    resultado = "Aprovado."
# entre 5 re 7    
elif nota >= 5:
    resultado = "Recuperação."
elif nota >= 4:
    resultado = "Conselho de classe."   
else:
    resultado = "Reprovado"






# Saída.
print(f"Resultado: {resultado}")