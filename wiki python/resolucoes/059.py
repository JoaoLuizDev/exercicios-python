"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

# criamos as variáveis, que armazenarão a quantidade de números pares e ímpares
quant_numero_par = 0
quant_numero_impar = 0

# laço de repetição, para a entrada dos dados, ou seja, dos 10 números
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))

# Verificamos se o número é par ou ímpar. Com o operador %, se o resto da divisão do número por 2 for igual a zero, par. 
# Caso contrário, número ímpar. 
    if numero % 2 == 0:
        quant_numero_par += 1
    else:
        quant_numero_impar += 1

print(f"Quantidade de números pares: {quant_numero_par}")
print(f"Quantidade de números ímpares: {quant_numero_impar}")
