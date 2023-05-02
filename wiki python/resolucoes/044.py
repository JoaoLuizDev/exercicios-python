"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

quant_morango = float(input("Digite quantos quilos de morango você quer comprar: "))
if quant_morango > 5:
    preço_morango = 2.2 * quant_morango
    print(f"R$ {preço_morango:.2f}.")
elif 0 <= quant_morango <= 5:
    preço_morango = 2.5 * quant_morango
    print(f"R$ {preço_morango:.2f}.")
else:
    print("ERRO.")
quant_maça = float(input("Digite quantos quilos de maçã você quer comprar: "))
if quant_maça > 5:
    preço_maça = 1.5 * quant_maça
    print(f"R$ {preço_maça:.2f}.")
elif 0 <= quant_maça <= 5:
    preço_maça = 1.8 * quant_morango
    print(f"R$ {preço_maça:.2f}.")
else:
    print("ERRO.")
quant_frutas = quant_morango + quant_maça
valor = preço_morango + preço_maça
if quant_frutas > 8 or valor > 25:
    total = valor - (valor / 100 * 10)
    desconto = valor - total
    print(f"Valor:    R$ {valor:.2f}\n"
          f"Desconto: R$ {desconto:.2f}\n---------------------------\n"
          f"TOTAL A SER PAGO: R$ {total:.2f}.")
else:
    print(f"TOTAL A SER PAGO: R$ {valor:.2f}")

