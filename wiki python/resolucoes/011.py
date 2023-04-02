"""
Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
    - o produto do dobro do primeiro com metade do segundo .
    - a soma do triplo do primeiro com o terceiro.
    - o terceiro elevado ao cubo.
"""

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
real = float(input("Informe um número real: "))
r1 = n1 * (n2 / 2)
r2 = (n1 * 3) + real
r3 = real ** 3
print(f"O produto do dobro do primeiro número informado com metade do segundo número informado é {r1:.2f}.")
print(f"A soma do triplo do primeiro informado com o terceiro número informado é igual a {r2:.2f}.")
print(f"O terceiro número informado elevado ao cubo é igual {r3:.2f}.")
