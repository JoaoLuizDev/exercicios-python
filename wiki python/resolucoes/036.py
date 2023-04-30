"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

print("Programa para pesquisar se estrutura de uma data segue o modelo dd/mm/aaaa.")
dia = int(input("Digite o dia com dois dígitos: "))
mes = int(input("Digite o mes com dois dígitos: "))
ano = int(input("Digite o ano com 4 dígitos: "))
print(f"A data digitada é {dia}/{mes}/{ano}.")

valida = False
    
# Meses com 31 dias
if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if(0 < dia <= 31):
        valida = True

# Meses com 30 dias
elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if(0 < dia <= 30):
        valida = True
elif mes == 2:
        
    # Testa se é bissexto
    if (ano% 4 == 0 and ano% 100 != 0) or (ano% 400 == 0):
        if(0 < dia <= 29):
            valida = True
        elif(dia <= 28):
            valida = True

if(valida):
    print('Essa data é válida')
else:
    print('Essa data é inválida')

"""
Explicação:
1- Criar variáveis "dia", "mes" e "ano";
2- Criar valor lógico verdadeiro ou falso, através da variável booleana "valido"; 
3- Indicamos valido = False;
4- Quantidade de dias por mês:
    28 dias - fevereiro;
    29 dias - fevereiro em ano bissexto;
    30 dias - abr/jun/set/nov;
    31 dias - jan/mar/maio/jul/ago/out/dez.
5- Verificar se os meses com 31 dias:
    True - se valores entre 1 e 31;
    False - se não atender à condição.
5- Verificar se os meses com 30 dias:
    True - se valores entre 1 e 30;
    False - se não atender à condição.
6- Verificar quantidade de dias de fevereiro:
    Bissexto - 
        True - se valores entre 1 e 29;
        False - se não atender à condição.
    Não bissexto -
        True - se valores entre 1 e 28;
        False - se não atender à condição.
7- Se a mês digitado não for entre 1 e 12, condição será False;
   Isso ocorre porque nos IF e ELIF, foram citados valores entre 1 e 12.
8- Por fim, se ao final do programa, a condição for True, a data é válida.
"""