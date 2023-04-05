"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

numero = float(input("Digite um núnero: "))
if numero > 0:
  print("O número informado é positivo.")
elif numero < 0:
  print("O número informado é negativo.")
else:
  print("O número é igual a zero.")
