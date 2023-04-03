"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
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
