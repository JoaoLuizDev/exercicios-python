"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""

print("Vamos analisar se um número qualquer é inteiro ou decimal.\n"
      "Caso digite um número decimal, utilize '.'(ponto) em vez de ',' (vírgula). ")
numero = float(input("Digite um número qualquer: "))

if numero == round(numero):
    print(f"O número {numero} é inteiro.")
else:
    print(f"O número{numero} é decimal.")