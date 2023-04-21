"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite outro numero: "))
numero_3 = float(input("Digite mais um numero: "))

if numero_1 > numero_2 > numero_3:
    print(numero_1, numero_2, numero_3)
elif numero_1 > numero_3 > numero_2:
    print(numero_1, numero_3, numero_2)
elif numero_2 > numero_1 > numero_3:
    print(numero_2, numero_1, numero_3)
elif numero_2 > numero_3 > numero_1:
    print(numero_2, numero_3, numero_1)
elif numero_3 > numero_1 > numero_2:
    print(numero_3, numero_1, numero_2)
else:
    print(numero_3, numero_2, numero_1)
