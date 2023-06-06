"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
"""

pais_a = 80000
taxa_a = 0.03
pais_b = 200000
taxa_b = 0.015
anos = 0

print("População do país A: 80000 habitantes.\n"
      "Taxa de crescimento: 3% ao ano.")
print("População do país B: 200000 habitantes.\n"
      "Taxa de crescimento: 1.5% ao ano."\n)
print("Em quantos anos a população do país A ultrapassará a do país B?")
while pais_a < pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    anos += 1

print(f'Após {anos} anos, a população do país A ultrapassará a do país B.')