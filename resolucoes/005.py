"""
Faça um Programa que converta metros para centímetros.
"""

metro = float(input("Digite a medida em metro a ser convertida em centímetro: "))
centimetro = metro * 100
print(f"A medida {metro:.2f}m é equivalente a {centimetro:.2f}cm.")

"""
Em {metro:.2f}, temos:
- metro --------- variável
- .2f   --------- uma especificação de formatação que indica que o número deve ser formatado com duas casas decimais 
                  e que deve ser exibido como um número de ponto flutuante.
                  Veja o exemplo a seguir.
"""

medida =  3.14159
print(f"{medida}")
print(f"{medida:.2f}")
