"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne
por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar.
"""

import sys

print("Escolha um dos tipos de carne na lista a seguir:\n"
      "Para FILÉ DUPLO, digite 1;\n"
      "Para ALCATRA, digite 2;\n"
      "Para PICANHA, digite 3.")
tipo = int(input("Digite a opção desejada: "))
if tipo == 1:
    quantidade = float(input("Digite quantos quilos de Filé Duplo você deseja comprar: "))
    if 0 < quantidade <= 5:
        valor_total = quantidade * 4.9
    elif quantidade > 5:
        valor_total = quantidade * 5.8
    else:
        print("ERRO. A quantidade deve ser maior que zero.")
elif tipo == 2:
    quantidade = float(input("Digite quantos quilos de Alcatra você deseja comprar: "))
    if 0 < quantidade <= 5:
        valor_total = quantidade * 5.9
    elif quantidade > 5:
        valor_total = quantidade * 6.8  
    else:
        print("ERRO. A quantidade deve ser maior que zero.")
elif tipo == 3:
    quantidade = float(input("Digite quantos quilos de Picanha você deseja comprar: "))
    if 0 < quantidade <= 5:
        valor_total = quantidade * 6.9
    elif quantidade > 5:
        valor_total = quantidade * 7.8
    else:
        print("ERRO. A quantidade deve ser maior que zero.")
else:
    print("Opção não encontrada.")
    sys.exit()

print("Formas de pagamento:\n"
      "1- dinheiro;\n"
      "2- cheque;\n"
      "3- cartão de débito;\n"
      "4- cartão de crédito;\n"
      "5- cartão Tabajara;\n"
      "6- pix.")
pagamento = int(input("Digite o número da forma de pagamento: "))
if pagamento == 5:
    valor_pagar = valor_total - (valor_total / 100 * 5)
    desconto = valor_total - valor_pagar
    print(f"\n----------------------\nTipo de carne: {tipo}\nQuantidade: {quantidade:.3f} kg\nVALOR TOTAL: R$ {valor_total:.2f}\nTipo de pagamento: {tipo}\n"
          f"Desconto: R$ {desconto:.2f}\nValor com desconto: R$ {valor_pagar:.2f}")
elif pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4 or pagamento == 6:
    print(f"\n----------------------\nTipo de carne: {tipo}\nQuantidade: {quantidade:.3f} kg\nTipo de pagamento: {tipo}\nVALOR TOTAL: R$ {valor_total:.2f}")
else:
    print("ERRO. Opção não encontrada.")
