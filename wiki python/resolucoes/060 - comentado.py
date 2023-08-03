"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

# primeiro, solicitamos ao usuário que indique quantos termos ele deseja consultar
termos = int(input("Digite o numero de termos da série de Fibonacci: "))

# variável "numero" com o valor inicial de 1, que representa o primeiro termo da sequência
numero = 1

# variável "numero_anterior" com o valor inicial de 0, que representa o termo anterior ao primeiro termo
numero_anterior = 0

#laço de repetição. O loop for irá executar o número de vezes especificado pelo usuário no input
for _ in range(termos):
    print(numero)                        # imprime o valor atual da variável numero, que é o termo atual da sequência
    aux = numero                         # variável "aux" para armazenar o valor atual da variável numero
    numero += numero_anterior            # atualiza o valor da variável numero somando-o ao valor da variável numero_anterior. 
    numero_anterior = aux                # atualiza o valor da variável numero_anterior com o valor anteriormente armazenado na variável aux. 
