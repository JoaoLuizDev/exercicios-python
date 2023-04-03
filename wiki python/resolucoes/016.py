"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

# Define a cobertura da tinta em metros quadrados por litro
cobertura_tinta = 3

# Define o tamanho da lata de tinta em litros e o preço
tamanho_lata = 18
preco_lata = 80.0

metros = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
quantidade_tinta = metros / cobertura_tinta
print(f"Serão necessários {quantidade_tinta:.2f} litros de tinta para pintar a área informada.")

# Calcula o número de latas de tinta necessárias, arredondando para cima
quantidade_latas = math.ceil(quantidade_tinta / tamanho_lata)

# Calcula o preço total das latas de tinta necessárias
preco_total = quantidade_latas * preco_lata

# Imprime na tela a quantidade de latas de tinta e o preço total
print(f"A quantidade de latas de tinta a serem compradas será de {quantidade_latas}.")
print(f"O valor gasto será de R$ {preco_total}.")


"""
Observação: 

math.ceil é uma função do módulo math em Python que retorna o menor número inteiro maior ou igual ao número fornecido.

Por exemplo, se você tem um número decimal como 2.5 e deseja arredondá-lo para cima para o próximo inteiro, 
você pode usar a função ceil da seguinte forma:

import math
numero_decimal = 2.5
numero_inteiro = math.ceil(numero_decimal)
print(numero_inteiro)

A saída seria 3, pois math.ceil(2.5) retorna o menor inteiro maior ou igual a 2.5, que é 3. 
No programa acima, ele arredonda o número para cima para garantir que tenha uma quantidade suficiente de tinta. 
"""
