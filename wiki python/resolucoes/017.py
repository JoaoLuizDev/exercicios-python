"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
"""

import math

# Define a cobertura da tinta em metros quadrados por litro
cobertura_tinta = 6         #metros por litro

# Define o tamanho da lata de tinta em litros, o preço e o tamanho do galão de tinta e o preço
tamanho_lata = 18           #litros
preco_lata = 80.0           #reais
tamanho_galao = 3.6         #litros
preco_galao = 25.0          #litros

tamanho_area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calcula a quantidade de tinta necessária em litros com 10% de folga, arredondando para cima
quantidade_tinta = math.ceil((tamanho_area / cobertura_tinta) * 1.1)
print(f"Serão necessários {quantidade_tinta} litros para pintar a área informada.")

apenas_latas = math.ceil(quantidade_tinta / tamanho_lata)
preco_apenas_latas = apenas_latas * preco_lata
print(f"Comprando apenas latas de 18 litros, você deverá comprar {apenas_latas} latas.")
print(f"O custo será de R$ {preco_apenas_latas}.")


apenas_galao = math.ceil(quantidade_tinta / tamanho_galao)
preco_apenas_galao = apenas_galao * preco_galao
print(f"Comprando apenas galão de 3.6 litros, você deverá comprar {apenas_galao} galões.")
print(f"O custo será de R$ {preco_apenas_galao}.\n")

print("Você pode comprar latas e galões. Vou te passar o orçamento.\n")

# Calcula o número de latas de tinta necessárias e o número de galões de tinta necessários, com base no tamanho e preço de cada recipiente
quantidade_latas = math.floor(quantidade_tinta / tamanho_lata)
quantidade_galoes = math.ceil((quantidade_tinta % tamanho_lata) / tamanho_galao)

# Calcula o preço total das latas de tinta e o preço total dos galões de tinta
preco_total_latas = quantidade_latas * preco_lata
preco_total_galoes = quantidade_galoes * preco_galao

print(f"Nesse caso, seria necessário comprar:\n"
      f"latas de tinta: {quantidade_latas}\n"
      f"preço total das latas de tinta: R$ {preco_total_latas}.\n"
      f"galões de tinta: {quantidade_galoes}.\n"
      f"preço total dos galões de tinta: R$ {preco_total_galoes}.")

# Calcula a quantidade de latas e galões de tinta para minimizar o desperdício de tinta
quantidade_latas_min = math.ceil((quantidade_tinta - (quantidade_galoes * tamanho_galao)) / tamanho_lata)
quantidade_galoes_min = math.ceil((quantidade_tinta - (quantidade_latas * tamanho_lata)) / tamanho_galao)

# Calcula o preço total para a combinação de latas e galões
preco_total_combinado = (quantidade_latas_min * preco_lata) + (quantidade_galoes_min * preco_galao)

print(f"Quantidade de latas e galões para minimizar o desperdício:")
print(f"Latas: {quantidade_latas_min}, Galões: {quantidade_galoes_min}.")
print(f"Preço total para essa combinação: R$ {preco_total_combinado}.")
