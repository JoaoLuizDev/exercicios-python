"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

for i in range(1, 21):          # Imprime do número 1 a 20
    print(i)                    # Imprime um abaixo do outro

for i in range(1, 21):          # Imprime do número 1 a 20
    print(i, end=' ')           # Imprime um ao lado do outro


# a função print(i) é chamada dentro de um loop for que itera de 1 a 20. A cada iteração, o valor atual de i é impresso em uma nova linha.

# a função print(i, end=' ') é chamada dentro de um loop for que também itera de 1 a 20. Os números serão impressos na mesma linha, separados por um espaço.