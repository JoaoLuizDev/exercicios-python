"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
"""

print("Vamos calcular uma equação de segundo grau?\n\n"
      "Forma: ax² + bx + c.\n")
a = float(input("Digite o valor do elemento A: "))
b = float(input("Digite o valor do elemento B: "))
c = float(input("Digite o valor do elemento C: "))
print(f"Equação: {a}x² + {b}x + c\n")
delta = (b ** 2) - 4 * a * c
if a == 0:
  print("De acordo com os valores informados, o A é igual a zero. Portanto, essa não é uma equação de segundo grau.")
elif delta < 0:
  print("Para resolver essa equação, usamos a chamada Fórmula de Bhaskara:\n"
        "Δ = b² - 4 * a * c\n"
       f"Δ = {delta}.")
  print("Quando o delta for negativo, a equação não possui raízes reais.")
else:
  print("Para resolver essa equação, usamos a chamada Fórmula de Bhaskara:\n"
  "Δ = b² - 4 * a * c")
  print(f"Δ = {delta}.\n")
  print("De acordo com os valores informados, a equação possuiu duas raízes reais.\n\n")
  dois_a = 2 * a
  raiz = delta ** (1/2)
  braiz_pos = - b + raiz
  braiz_neg = - b - raiz
  x_um = braiz_pos / dois_a
  x_dois= braiz_neg / dois_a
  print("Fórmula para calcular as raízes:\n"
        "x1 = (-b + (Δ ** (1/2)) / 2 * a \n"
       f"x1 = (-{b} + ({delta} ** (1/2)) / 2 * {a} \n"
       f"x1 = (-{b} + {raiz}) / {dois_a} \n"
       f"x1 = {braiz_pos} / {dois_a} \n"
       f"x1 = {x_um}\n\n")

  print("x2 = (-b - (Δ ** (1/2)) / 2 * a \n"
       f"x2 = (-{b} - ({delta} ** (1/2)) / 2 * {a} \n"
       f"x2 = (-{b} - {raiz}) / {dois_a} \n"
       f"x2 = {braiz_neg} / {dois_a} \n"
       f"x2 = {x_dois}\n\n")
  # fiz a resolução passo a passo. Caso prefira, basta executar o código a seguir e chegará ao mesmo resultado
  x1 = (- b + (delta ** (1/2))) / (2 * a)
  x2 = (- b - (delta ** (1/2))) / (2 * a)
  print(f"x1= {x1} \nx2 = {x2}\n")
  print(f"x1= {x1:.2f} \nx2 = {x2:.2f}")
  
