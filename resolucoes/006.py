"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

print("Vamos calcular a área do círculo.")
raio = float(input("Para isso, digite o raio do círculo: "))
π = 3,14
r = raio ** 2
area = 3.14 * (r ** 2)
print(f"O círculo que tem o raio igual a {raio:.2f}, terá a área de {area:.2f}.")

print("\nÁrea = π * r²")
print(f"Área = {π} * {raio:.2f}²")
print(f"Área = {π} * {r:.2f}")
print(f"Área = {area:.2f}")
