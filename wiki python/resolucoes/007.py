"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

# variável com número inteiro
print("Vamos calcular a área de um quadrado qualquer?")
lado = int(input("Digite a medida, em centímetros, de um dos lados do quadrado: "))
area = lado * lado
dobro = area * 2
print(f"A área do quadrado com a medida informada é de {area} cm.")
print(f"O dobro da área desse quadrado é igual a {dobro} cm.")

# variável com número decimal
print("Vamos calcular a área de um quadrado qualquer?")
lado = float(input("Digite a medida, em centímetros, de um dos lados do quadrado: "))
area = lado * lado
dobro = area * 2
print(f"A área do quadrado com a medida informada é de {area} cm.")
print(f"O dobro da área desse quadrado é igual a {dobro} cm.")
