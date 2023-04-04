"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho = float(input("Informe o tamanho do arquivo, em MB, que você deseja fazer download: "))
velocidade = float(input("Informe, em Mbps, a velocidade da sua conexão:"))
tempo = tamanho / (velocidade / 8)
minutos = tempo // 60
segundos = tempos % 60
print("A fórmula para calcular é:\n"
      "Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.\n")
print(f"O tempo para completar o download será de {minutos:.0f} minutos e {segundos:.0f} segundos.")


"""
Observação:
            minutos = tempo // 60 ------- esta linha calcula a quantidade de minutos no tempo estimado de download, 
                                          dividindo o valor armazenado na variável tempos por 60 e arredondando para 
                                          baixo (usando o operador "//" para divisão de números inteiros).
            
            segundos = tempos % 60 ------ esta linha calcula o número de segundos restantes no tempo estimado de download, 
                                          calculando o resto da divisão do valor armazenado na variável tempos por 60 
                                          (usando o operador "%" para módulo).
"""
