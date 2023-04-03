"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos),
deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""


print("Olá, João Papo-de-Pescador.")
peso = float(input("Informe o peso, em kg, da carga de peixe pescada hoje: "))
excesso = peso - 50
multa = excesso * 4
print("De acordo com o regulamento de pesca do estado de São Paulo, o limite é de 50kg.")
print(f"Portanto, hoje, o excesso foi de {excesso:.2f}kg.")
print(f"Dessa forma, o valor da multa a ser paga será de R${multa:.2f}.")




"""

Observação:
O código apresentado é funcional somente se o peso da pesca for maior que 50kg.
Caso contrário, o código apresentará erro. 
A solução seria usar estrutura condicional, porém não foi utilizada tendo em vista que a ideia dessa lista de resoluções é seguir 
uma ordem de complexidade crescente, do mais simples ao mais complexo, auxiliando quem está começando a estudar Python
"""
