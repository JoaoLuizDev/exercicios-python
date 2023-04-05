"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


# a resolução abaixo atende ao que foi pedido, porém se o usuário digitar um número, mais de uma letra ou outro tipo de caracter, a resposta será "consoante".

letra = input("Digite uma letra: ").strip().lower()
if letra in 'aeiou':
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")


# agora, o código só aceitará letras. porém, se o usuário digitar mais de uma letra, ainda assim terá uma resposta.

letra = input("Digite uma letra: ").strip().lower()
if letra in 'aeiou':
    print("A letra digitada é uma vogal.")
# Verificar se a letra é uma consoante
elif letra.isalpha():
    print("A letra digitada é uma consoante.")
else:
    print("Entrada inválida. Por favor, digite apenas uma letra do alfabeto.")
   
# finalmente, nesse código só é aceito uma letra.
letra = input("Digite uma letra: ").strip().lower()
if letra.isalpha() and len(letra) == 1:
    if letra in 'aeiou':
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("Por favor, digite apenas uma letra.")
