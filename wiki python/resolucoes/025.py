"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

print("Por favor, digite a seguir 3 números.")
numero_1 = float(input("Digite um número qualquer: "))
numero_2 = float(input("Digite outro número qualquer: "))
numero_3 = float(input("Digite outro número qualquer: "))

print(f"Você digitou {numero_1}, {numero_2} e {numero_3}.")
if numero_3 < numero_1 > numero_2:
  print(f"O maior número é {numero_1}.")
elif numero_1 < numero_2 > numero_3:
  print(f"O maior número é {numero_2}.")
else:
  print(f"O maior número é {numero_3}.")

if numero_2 > numero_1 < numero_3:
  print(f"O menor número é {numero_1}.")
elif numero_1 > numero_2 < numero_3:
  print(f"O menor número é o {numero_2}.")
else:
  print(f"O menor número é o {numero_3}.")
