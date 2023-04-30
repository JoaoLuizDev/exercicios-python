"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

print("O limite diário de saque é de R$ 600.")
saque = float(input("Digite o valor que deseja sacar: "))
if 10 <= saque <= 600:
    print(f"O valor do saque é de R$ {saque:.2f}.")
    nota_100 = saque // 100
    saque = saque - (nota_100 * 100)
    nota_50 = saque // 50
    saque = saque - (nota_50 * 50)
    nota_10 = saque // 10
    saque = saque - (nota_10 * 10)
    nota_5 = saque // 5
    saque = saque - (nota_5 * 5)
    nota_1 = saque // 1
    print("Você receberá:\n"
          f"{nota_100:.0f} cédula(s) de R$100,00\n"
          f"{nota_50:.0f} cédula(s) de R$ 50,00\n"
          f"{nota_10:.0f} cédula(s) de R$ 10,00\n"
          f"{nota_5:.0f} cédula(s) de R$ 05,00\n"
          f"{nota_1:.0f} cédula(s) de R$ 01,00")
elif 10 > saque > 1000:
    print("O valor é maior que o limite diário de saque.")
else:
    print("Valor não permitido.")
