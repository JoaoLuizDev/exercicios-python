"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

'''nota = float(input("Digite uma nota, entre zero e 10: "))
while nota < 0 or nota > 10:
    print("Nota inválida. Tente novamente.")
    nota = float(input("Digite uma nota, entre zero e 10: ")) # Não é necessário, mas é bom para o usuário saber o que está fazendo.
if 0 <= nota <= 10:
    print("Nota válida.")

print(f"Você digitou a nota {nota}.")

'''
"""Outra forma de fazer:"""

while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Valor inválido. Por favor, digite novamente.")

print(f"Você digitou a nota {nota}.")

