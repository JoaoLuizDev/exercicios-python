"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

print("Vamos analisar se um número qualquer é par ou ímpar.")
numero = int(input("Digite um número inteiro: "))
analise = numero % 2
if analise == 0:
  print(f"O número {numero} é par.")
else:
  print(f"O número {numero} é ímpar.")
