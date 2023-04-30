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

# 1-) identicar valor da unidade.
unidade = numero % 10                         

"""
O operador % é o módulo de divisão. 
Exemplo: 11 % 3 = 2 --------- Se dividirmos 11 unidades em 3 grupos com a mesma quantidade entre si, teremos 3 grupos com 3 unidades; e 2 de resto.
                              Com o operador %, conseguimos identificar o valor do resto da divisão. 
"""

# 2-) Atualizar número que ainda será trabalhado.
numero = (numero - unidade)/10

"""
Após identificarmos o valor da unidade, devemos retira-lo para encontrar a dezena e centena.
Exemplo:  99                                            
          99 % 10 = 9 unidades                          
          99 - 9 = 90
Note que ocorreu uma divisão por 10. Dessa forma, já sabemos que quantas dezenas nosso número tem.
90 / 10 = 9 dezenas
Mas, em números maiores que 99, ocorre um problema, pois o código não identifica centena. 
Exemplo:  587
          587 % 10 = 7 unidades 
          587 -7 = 580   
          58 / 10 = 58 dezenas                                                                                                   
"""

# Extraindo a dezena
dezena = numero % 10

"""
Para resolver o problema, 
Exemplo:  587
          587 % 10 = 7 unidades 
          587 -7 = 580   
          58 / 10 = 58                                                                                                   
          58 % 10 = 8 dezenas
"""

# Eliminando a dezena do número original, fica a centena
centena = (numero - dezena)/10

"""
Momento de identificar a quantidade de centenas.
Exemplo:  587
          587 % 10 = 7 unidades 
          587 -7 = 580   
          58 / 10 = 58                                                                                                   
          58 % 10 = 8 dezenas
          58 - 8 = 50
Até ponto, encontramos a quantidade de dezenas. Basta dividir por 10 e teremos o número de centenas.
          50 / 10 = 5 centenas
"""

print(f"{centena:.0f} centena(s),', {dezena:.0f} 'dezena(s)' e {unidade:.0f} 'unidade(s)'.")