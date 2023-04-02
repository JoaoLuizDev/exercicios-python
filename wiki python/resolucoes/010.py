"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

print("Programa para conversão de temperatura em graus Celsius para graus Fahrenheit.")
C = float(input("Digite a temperatura em graus celsius: "))
F = (C * 1.8) + 32
print(f"A temperatura {C}º F é equivalente a {F:.2f}º C.") 
