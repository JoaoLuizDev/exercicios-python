"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"As notas bimestrais foram {nota1:.2f}, {nota2:.2f}, {nota3:.2f} e {nota4:.2f}."
      f"\nA nota média foi de {media:.2f}.")
