"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""

n1 = float(input("Digite um número qualquer: "))
n2 = float(input("Digite outro número: "))
print("Escolha qual operação matemática você deseja realizar, seguindo o modelo abaixo:\n"
      "1- adição;\n2- subtração;\n3- multiplicação;\n4- divisão.")
operacao = int(input("Digite o número da opção desejada: "))
if operacao == 1 or 2 or 3 or 4:
    if operacao == 1:
        numero = n1 + n2
        print(f"Resultado: {numero}.")
    elif operacao == 2:
        numero = n1 - n2
        print(f"Resultado: {numero}.")
    elif operacao == 3:
        numero = n1 * n2
        print(f"Resultado: {numero}.")
    elif operacao == 4:
        numero = n1 / n2
        print(f"Resultado: {numero}.")
    
    if numero == round(numero):
      print("Inteiro.")
    else:
      print("Decimal.")

    analise = numero % 2
    if analise == 0:
      print("Par.")
    else:
      print("Ímpar.")

    if numero == 0:
      print("O número 0 é neutro.")
    elif numero > 0:
      print("Positivo.")
    else:
      print("Negativo.")
else:
  print("Opção não encontrada.")

