"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota: "))
media = (nota_1 + nota_2) / 2
if media >= 7:
  print(f"Sua média foi de {media}.")
  print("Aprovado. Parabéns.")
elif media == 10:
  print(f"Sua média foi de {media}.")
  print("Aprovado com Distinção.")
elif 0 < media < 7:
  print(f"Sua média foi de {media}.")
  print("Reprovado.")
else:
  print("Erro. Tente novamente.")
