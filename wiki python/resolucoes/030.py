"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

horas = int(input("Quantas horas você trabalhou no mês? "))
valor = float(input("Quanto você recebe por hora? "))
salario_bruto = horas * valor
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if salario_bruto < 0:
  print("Dados incorretos.")
elif salario_bruto == 0:
  print("Você está desempregado.")
elif salario_bruto <= 900:
  descontos = inss + fgts
  salario_liquido = salario_bruto - descontos
  print(f"Salário Bruto: ({horas} * {valor})      : R$ {salario_bruto:.2f}\n"
        f"(-) IR (isento)                 : R$  00.00\n"
        f"(-) INSS ( 10%)                 : R$  {inss:.2f}\n"
        f"FGTS (11%)                      : R$  {fgts:.2f}\n"
        f"Total de descontos              : R$  {descontos:.2f}\n"
        f"Salário Liquido                 : R$ {salario_liquido:.2f}")
elif salario_bruto <= 1500:
  ir = salario_bruto * 0.05
  descontos = inss + fgts + ir
  salario_liquido = salario_bruto - descontos
  print(f"Salário Bruto: ({horas} * {valor})      : R$ {salario_bruto:.2f}\n"
        f"(-) IR (5%)                     : R$   {ir:.2f}\n"
        f"(-) INSS ( 10%)                 : R$  {inss:.2f}\n"
        f"FGTS (11%)                      : R$  {fgts:.2f}\n"
        f"Total de descontos              : R$  {descontos:.2f}\n"
        f"Salário Liquido                 : R$ {salario_liquido:.2f}")
elif salario_bruto <= 2500:
  ir = salario_bruto * 0.1
  descontos = inss + fgts + ir
  salario_liquido = salario_bruto - descontos
  print(f"Salário Bruto: ({horas} * {valor})      : R$ {salario_bruto:.2f}\n"
        f"(-) IR (10%)                    : R$  {ir:.2f}\n"
        f"(-) INSS ( 10%)                 : R$  {inss:.2f}\n"
        f"FGTS (11%)                      : R$  {fgts:.2f}\n"
        f"Total de descontos              : R$  {descontos:.2f}\n"
        f"Salário Liquido                 : R$ {salario_liquido:.2f}")
else:
  ir = salario_bruto * 0.2
  descontos = inss + fgts + ir
  salario_liquido = salario_bruto - descontos
  print(f"Salário Bruto: ({horas} * {valor})     : R$  {salario_bruto:.2f}\n"
        f"(-) IR (20%)                    : R$  {ir:.2f}\n"
        f"(-) INSS ( 10%)                 : R$   {inss:.2f}\n"
        f"FGTS (11%)                      : R$   {fgts:.2f}\n"
        f"Total de descontos              : R$  {descontos:.2f}\n"
        f"Salário Liquido                 : R$  {salario_liquido:.2f}")
