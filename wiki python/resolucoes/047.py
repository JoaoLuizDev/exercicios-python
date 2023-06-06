"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while True:
    nome = str(input("Digite o nome do usuário: "))
    senha = input("Digite a senha: ")
    if nome == senha:
        print("Erro: o nome de usuário e a senha devem ser diferentes.")
    else:
        break

print("Usuário cadastrado com sucesso!")