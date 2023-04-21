"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produto_1 = float(input("Digite o preço do primeiro produto: "))
produto_2 = float(input("Digite o preço do segundo produto: "))
produto_3 = float(input("Digite o preço do terceiro produto: "))

if produto_2 > produto_1 < produto_3:
  print(f"Entre os produtos informados, o primeiro produto, no valor de R$ {produto_1:.2f} é o mais barato.")
  print("Recomendação de compra: produto 1.")
elif produto_1 > produto_2 < produto_3:
  print(f"Entre os produtos informados, o segundo produto, no valor de R$ {produto_2:.2f} é o mais barato.")
  print("Recomendação de compra: produto 2.")
else:
  print(f"Entre os produtos informados, o terceiro produto, no valor de R$ {produto_3:.2f} é o mais barato.")
  print("Recomendação de compra: produto 3.")
