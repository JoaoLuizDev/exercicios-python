"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

print("Vamos analisar a figura geométrica?")
lado_1 = float(input("Digite a medida do primeiro lado: "))
lado_2 = float(input("Digite a medida do segundo lado: "))
lado_3 = float(input("Digite a medida do terceiro lado: "))
if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
  print("Os valores informados formam um triângulo.")
  if lado_1 == lado_2 and lado_2 == lado_3:
    print("Por ter 3 lados com valores iguais, ele recebe o nome de Triângulo Equilátero.")
  elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Por ter 2 lados com valores iguais, ele recebe o nome de Triângulo Isósceles.")
  else:
    print("Por ter 3 lados com valores diferentes, ele recebe o nome de Triângulo Escaleno.")
else:
  print("Os valores informados não formam um triângulo.")
