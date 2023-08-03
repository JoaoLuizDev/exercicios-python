"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input('Digite um número para calcular seu fatorial: '))
    # O programa solicita ao usuário que digite um número inteiro. Esse número será usado para calcular o fatorial.

c = numero
    # é criada uma variável chamada c com valor de numero, que será usada como um contador para o loop que calcula o fatorial.

f = 1
    # criada uma variável f com valor 1. Essa variável será usada para acumular o resultado do cálculo do fatorial.

print(f'Calculando {numero}! = ', end='')
    # Essa linha imprime a mensagem que mostra como o cálculo fatorial acontece. 
    # O parâmetro end='' é usado para evitar que a próxima saída seja impressa em uma nova linha.

while c > 0:
    # loop while continuará enquanto o valor de c for maior que zero.

    print(f'{c}', end='')
    # imprime o valor atual de c, que representa o número para o qual estamos calculando o fatorial.

    print(' x ' if c > 1 else ' = ', end='')
    # Esta linha imprime ' x ' se o valor de c for maior que 1, indicando que estamos multiplicando. 
    # Caso contrário, imprime ' = ' para mostrar que estamos no último passo do cálculo.     
     
    f *= c
    # o valor atual de c é multiplicado ao acumulador f. Isso efetivamente realiza o cálculo do fatorial.

    c -= 1
    # o valor de c é decrementado em 1, preparando-se para o próximo passo do cálculo.

print(f'{f}')
    # imprime o resultado final do cálculo do fatorial.