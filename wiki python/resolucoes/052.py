"""
Faça um programa que leia 5 números e informe o maior número.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))
n5 = int(input("Digite outro número: "))

maior = n1                                          # criado variável chamada maior e inicializada com o valor de n1. 
                            
if n2 > maior:
    maior = n2
                            # Se algum desses números for maior do que o valor atual de maior, a variável maior é atualizada com o novo valor.
if n3 > maior:  
    maior = n3

if n4 > maior:
    maior = n4

if n5 > maior:
    maior = n5

print(f"O maior número é {maior}.")