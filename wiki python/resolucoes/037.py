"""
Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com:
1, 7, 10, 11, 16, 20, 21, 25, 100, 101, 111, 300, 301, 305, 310, 311, 320, 326
"""

numero = int(input('Digite um numero inteiro positivo entre 1 e 999: '))

unidade = numero % 10

numero = (numero - unidade)/10

dezena = numero % 10

centena = (numero - dezena)/10

print(f"{centena:.0f} centena(s),', {dezena:.0f} 'dezena(s)' e {unidade:.0f} 'unidade(s)'.")
