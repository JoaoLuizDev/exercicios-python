"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

print("Nesse programa, vamos calcular o peso ideal de uma pessoa a partir da altura.")
print("A altura deve ser informada em metros, seguindo o modelo a seguir: 1.78m.\nVamos começar?")
altura = float(input("Informe a altura em metros: "))
peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7
print(f"Para um homem com {altura:.2f}m de altura, o peso ideal é de {peso_homem:.2f}.")
print(f"Para uma melher com {altura:.2f}m de altura, o peso ideal é de {peso_mulher:.2f}kg.")
