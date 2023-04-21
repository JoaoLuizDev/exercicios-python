"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.
"""

nota_1 = float(input("Digite a 1º nota parcial (0 a 10): "))
if 10 >= nota_1 >= 0:
  nota_2 = float(input("Digite a 2º nota parcial (0 a 10): "))
  if 10 >= nota_2 >= 0:
    media = (nota_1 + nota_2) / 2
    print("Critérios para atribuição de nota:\n"
              "\n    Média de Aproveitamento  Conceito\n"
              "       Entre 9.0 e 10.0         A\n"
              "       Entre 7.5 e 9.0          B\n"
              "       Entre 6.0 e 7.5          C\n"
              "       Entre 4.0 e 6.0          D\n"
              "       Entre 4.0 e zero         E\n")
    if 0 <= media <= 4: 
        print(f"A média das suas notas é {media}.\nO conceito é 'E'.\nREPROVADO.")
    elif 4 < media >= 6:
        print(f"A média das suas notas é {media}.\nO conceito é 'D'.\nREPROVADO.")
    elif 6 < media >= 7.5:
        print(f"A média das suas notas é {media}.\nO conceito é 'C'.\nAPROVADO.")
    elif 7.5 < media >= 9:
        print(f"A média das suas notas é {media}.\nO conceito é 'B'.\nAPROVADO.")
    else:  
        print(f"A média das suas notas é {media}.\nO conceito é 'A'.\nAPROVADO.")
  else:
      print("Dados inválidos.")
else:
  print("Dados inválidos.")
