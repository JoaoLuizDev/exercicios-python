"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Iniciamos o resultado com 1 porque, quando multiplicamos um número por 1, o resultado é igual a esse número. 
resultado = 1

# no laço de repetição abaixo, será repetida a operação pelo número de vezes igual ao valor do expoente.  
for _ in range(expoente):
    resultado *= base

# a linha acima equivale a resultado = resultado * base

print(f"O resultado de {base} elevado a {expoente} é: {resultado}.")
