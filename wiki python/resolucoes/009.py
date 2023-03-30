"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

print("Programa para conversão de temperatura em graus Fahrenheit para graus Celsius.")
F = float(input("Digite a temperatura em graus farenheit: "))
C = 5 * ((F-32) / 9)
print(f"A temperatura {F}º F é equivalente a {C:.2f}º C.") 
