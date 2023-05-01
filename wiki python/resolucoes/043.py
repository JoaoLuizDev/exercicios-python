"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

tipo = str(input("Qual o tipo de combustível?\nDigite G para gasolina e A para álcool: "))
litros = float(input("Digite a quantidade de litros vendida: "))
if tipo == "G":
    if 0 < litros <= 20:
        desconto = 2.5 - (2.5 / 100 * 3)
        valor = litros * desconto
        preço = 2.5 * litros
        economia = preço - valor
        print(f"O valor sem desconto seria de R$ {preço:.2f}.\nDesconto: R$ {economia:.2f}.\n\nTOTAL: R$ {valor:.2f}.")
    elif litros > 20:
        desconto = 2.5 - (2.5 / 100 * 5)
        valor = litros * desconto
        preço = 2.5 * litros
        economia = preço - valor
        print(f"O valor sem desconto seria de R$ {preço:.2f}.\nDesconto: R$ {economia:.2f}.\n\nTOTAL: R$ {valor:.2f}.")
    else:
        print("ERRO")
elif tipo == "A":
    if 0 < litros <= 20:
        desconto = 1.9 - (1.9 / 100 * 4)
        valor = litros * desconto
        preço = 1.9 * litros
        economia = preço - valor
        print(f"O valor sem desconto seria de R$ {preço:.2f}.\nDesconto: R$ {economia:.2f}.\n\nTOTAL: R$ {valor:.2f}.")
    elif litros > 20:
        desconto = 1.9 - (1.9 / 100 * 6)
        valor = litros * desconto
        preço = 1.9 * litros
        economia = preço - valor
        print(f"O valor sem desconto seria de R$ {preço:.2f}.\nDesconto: R$ {economia:.2f}.\n\nTOTAL: R$ {valor:.2f}.")
    else:
        print("ERRO")
else:
    print("ERRO")