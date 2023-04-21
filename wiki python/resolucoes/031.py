"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

numero = int(input("Qual seu dia da semana favorito?\nEscolha o dia da semana conforme lista abaixo:\n"
                   "1- Domingo;\n2- Segunda;\n3- Terça;\n4- Quarta;\n5- Quinta;\n6- Sexta;\n7- Sábado.\n"
                   "\nDigite o número correspondente ao dia da semana: "))

if numero == 1:
  print("Seu dia da semana favorito é DOMINGO.")
elif numero == 2:
  print("Seu dia da semana favorito é SEGUNDA-FEIRA.")
elif numero == 3:
  print("Seu dia da semana favorito é TERÇA-FEIRA.")
elif numero == 4:
  print("Seu dia da semana favorito é QUARTA-FEIRA.")
elif numero == 5:
  print("Seu dia da semana favorito é QUINTA-FEIRA.")
elif numero == 6:
  print("Seu dia da semana favorito é SEXTA-FEIRA.")
elif numero == 7:  
  print("Seu dia da semana favorito é SÁBADO.")
else:
  print("Valor inválido.")
