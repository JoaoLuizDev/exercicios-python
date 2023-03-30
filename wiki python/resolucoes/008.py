"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

# Cálculo de salário por horas trabalhadas
valor = float(input("Qual o valor da sua remuneração por hora? "))
horas = int(input("Quantas horas você trabalhou no mês analisado? "))
salario = valor * horas
print(f"Com a remuneração de {valor:.2f}, trabalhando {horas} por mês, o valor do salário no referido mês é de {salario:.2f}.")


# Cálculo de salário por dias e horas trabalhadas
valor = float(input("Qual o valor da sua remuneração por hora? "))
horas = int(input("Qual sua carga horária diária? "))
dias = int(input("Quantos dias você trabalhou no mês analisado? "))
salario = valor * horas * dias
print(f"Com a remuneração de {valor:.2f}, o valor do salário no referido mês é de {salario:.2f}.")
