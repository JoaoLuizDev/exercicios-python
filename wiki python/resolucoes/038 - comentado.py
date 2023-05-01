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
# 1-) criamos a condição - valor deve ser maior ou igual a 10 e menor ou igual a 1000.
if 10 <= saque <= 600:
    print(f"O valor do saque é de R$ {saque:.2f}.")

# 2-) calculamos a quantidade de notas 100 que poderiam ser entregues ao cliente.
    nota_100 = saque // 100
"""
O operador // significa divisão inteira, ou seja, o resultado será o maior número inteiro possível. 
Exemplo:
87  / 4 = 21.25 
87 // 4 = 21 

Usando esse operador no código, teremos quantas notas de 100 seriam entregues.
Exemplo:
500 // 100 = 5
550 // 100 = 5
 89 // 100 = 0
"""
# 3-) atualizamos o valor a ser calculado após a entrega (ou não) das notas de 100
    saque = saque - (nota_100 * 100)
"""
Aqui, substraímos do valor digitado o valor correspondente às notas de 100 entregues.
Exemplo:
587 // 100 = 5 notas de 100
saque = 587 - 5 * 100
saque = 587 - 500
saque = 87 reais
"""

# 4-) calculamos, sob o valor restante, a quantidade de notas 50 que poderiam ser entregues ao cliente.
    nota_50 = saque // 50
"""
Seguindo o exemplo anterior:
587 // 100 = 5 notas de 100
saque = 587 -500
saque = 87
87 // 50 = 1 nota de 50
"""

# 5-) atualizamos o valor a ser calculado após a entrega (ou não) das notas de 50
    saque = saque - (nota_50 * 50)
"""
Exemplo:
87 - 1 * 50 
87 - 50
87 -50 = 37
"""

# 6-) calculamos, sob o valor restante, a quantidade de notas 10 que poderiam ser entregues ao cliente.
    nota_10 = saque // 10
"""
Seguindo o exemplo anterior:
37 // 10 = 3 notas de 10
"""

# 7-) atualizamos o valor a ser calculado após a entrega (ou não) das notas de 10
    saque = saque - (nota_10 * 10)
"""
Exemplo:
37 - 3 * 10
37 - 30 = 7
"""

# 8-) calculamos, sob o valor restante, a quantidade de notas de 5 que poderiam ser entregues ao cliente.
    nota_5 = saque // 5
"""
Seguindo o exemplo anterior:
7 // 5 = 1 nota de 5
"""

# 9-) atualizamos o valor a ser calculado após a entrega (ou não) das notas de 5
    saque = saque - (nota_5 * 5)
"""
Exemplo:
7 - 1 * 5
7 -5 = 2
"""

# 10-) calculamos, sob o valor restante, a quantidade de notas de 1 que poderiam ser entregues ao cliente.
    nota_1 = saque // 1
"""
Seguindo o exemplo anterior:
2 // 1 = 2 notas de 1
"""

    print("Você receberá:\n"
          f"{nota_100:.0f} cédula(s) de R$100,00\n"
          f"{nota_50:.0f} cédula(s) de R$ 50,00\n"
          f"{nota_10:.0f} cédula(s) de R$ 10,00\n"
          f"{nota_5:.0f} cédula(s) de R$ 05,00\n"
          f"{nota_1:.0f} cédula(s) de R$ 01,00")
elif 10 > saque > 1000:
    print("OPERAÇÃO NÃO REALIZADA - O valor é maior que o limite diário de saque.")
else:
    print("Valor não permitido.")
