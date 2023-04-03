"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

import math

tamanho = float(input("Informe o tamanho do arquivo, em MB, que você deseja fazer download: "))
velocidade = float(input("Informe, em Mbps, a velocidade da sua conexão:"))
tempo = tamanho / (velocidade / 8)
minutos = tempo / 60
minutos_arredondados = math.ceil(minutos)
print("A fórmula para calcular é:\n"
      "Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.\n")
print(f"O tempo para completar o download será de {tempo:.2f} segundos, ou, arredondando para cima, {minutos_arredondados} minutos.")
