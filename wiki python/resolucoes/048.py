"""
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

print("Programa de cadastro de funcioanários")
while True:
    nome = str(input("Digite seu nome: "))
    if len(nome) > 3:
        break
    else:
        print("Erro: o nome deve ter mais de 3 caracteres.")
        print("Tente novamente.")

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade < 150:
        break
    else:
        print("Erro: a idade deve estar entre 0 e 150.")
        print("Tente novamente.")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Erro: o salário deve ser maior que zero.")
        print("Tente novamente.")

while True:
    sexo = str(input("Digite seu sexo (M/F): ")).upper().strip()
    if sexo == "M" or sexo == "F":
        break
    else:
        print("Erro: o sexo deve ser M ou F.")
        print("Tente novamente.")

while True:
    civil = str(input("Digite seu estado civil (S/C/V/D): ")).upper().strip()
    if civil == "S" or civil == "C" or civil == "V" or civil == "D":
        break
    else:
        print("Erro: o estado civil deve ser S, C, V ou D.")
        print("Tente novamente.")

"""outra resolução: """

nome = input("Digite o nome (maior que 3 caracteres): ")
while len(nome) <= 3:
    print("Nome inválido. O nome deve ter mais de 3 caracteres.")
    nome = input("Digite o nome (maior que 3 caracteres): ")

idade = int(input("Digite a idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
    print("Idade inválida. A idade deve estar entre 0 e 150.")
    idade = int(input("Digite a idade (entre 0 e 150): "))

salario = float(input("Digite o salário (maior que zero): "))
while salario <= 0:
    print("Salário inválido. O salário deve ser maior que zero.")
    salario = float(input("Digite o salário (maior que zero): "))

sexo = input("Digite o sexo ('f' ou 'm'): ")
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido. O sexo deve ser 'f' ou 'm'.")
    sexo = input("Digite o sexo ('f' ou 'm'): ")

estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Estado civil inválido. O estado civil deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ")

print("Informações válidas!")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
