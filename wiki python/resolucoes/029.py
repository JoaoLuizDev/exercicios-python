"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    - salários até R$ 280,00 (incluindo): aumento de 20%;
    - salários entre R$ 280,00 e R$ 700,00: aumento de 15%;
    - salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
    - salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado.

Informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.
"""

salario_atual = float(input("Digite o valor do seu salário atualmente: "))
if salario_atual == 0:
  print("Você está desempregado.") 

elif salario_atual < 0:
  print("Valor incorreto.")

elif salario_atual <= 280:
  aumento = salario_atual * 0.2
  salario_novo = salario_atual + aumento
  print(f"O seu salário hoje é de R$ {salario_atual:.2f}.\nSeu aumento será de 20%.\nO valor do aumento será de R$ {aumento:.2f}.\n"
        f"O novo valor do salário será de R$ {salario_novo:.2f}.")

elif 280 < salario_atual <= 700:
  aumento = salario_atual * 0.15
  salario_novo = salario_atual + aumento  
  print(f"O seu salário hoje é de R$ {salario_atual:.2f}.\nSeu aumento será de 15%.\n"
        f"O valor do aumento será de R$ {aumento:.2f}.\n"
        f"O novo valor do salário será de R$ {salario_novo:.2f}.")
  
elif 700 < salario_atual <= 1500:
  aumento = salario_atual * 0.1
  salario_novo = salario_atual + aumento
  print(f"O seu salário hoje é de R$ {salario_atual:.2f}.\nSeu aumento será de 10%.\n"
        f"O valor do aumento será de R$ {aumento:.2f}.\n"
        f"O novo valor do salário será de R$ {salario_novo:.2f}.")
  
else:
  aumento = salario_atual * 0.05
  salario_novo = salario_atual + aumento
  print(f"O seu salário hoje é de R$ {salario_atual:.2f}.\nSeu aumento será de 5%.\n"
        f"O valor do aumento será de R$ {aumento:.2f}.\n"
        f"O novo valor do salário será de R$ {salario_novo:.2f}.") 
