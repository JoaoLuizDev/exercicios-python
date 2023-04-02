"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

print("Nesse programa, vamos calcular o peso ideal de uma pessoa a partir da altura.")
print("A altura deve ser informada em metros, seguindo o modelo a seguir: 1.78m.\nVamos começar?")
altura = float(input("Informe a altura em metros: "))
peso_ideal = (72.7 * altura) - 58
print(f"O peso ideal de uma pessoa com {altura}m de altura é igual a {peso_ideal:.2f}kg.")
