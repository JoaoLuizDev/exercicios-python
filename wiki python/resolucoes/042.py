"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    ""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

print("Olá, esse programa simula um interrogatório.\n"
      "Após as perguntas, será emitido uma classificação sobre a participação do usuário no crime.\n"
      "Para responder 'SIM', digite 1. Para responder 'NÃO', digite 0.")
p1 = int(input("Telefonou para a vítima?"))
if p1 == 0 or 1:
    p2 = int(input("Esteve no local do crime?"))
    if p2 == 0 or 1:
        p3 = int(input("Mora perto da vítima?"))
        if p3 == 0 or 1:
            p4 = int(input("Devia para a vítima?"))
            if p4 == 0 or 1:
                p5 = int(input("Já trabalhou com a vítima?"))
                if p5 == 0 or 1:
                    soma = p1 + p2 + p3 + p4 + p5
                    if soma == 1:
                        print("Você é INOCENTE.")
                    elif soma == 2:
                        print("Você é considerado SUSPEITO.")
                    elif soma == 3 or 4:
                        print("Você é considerado CÚMPLICE.")
                    else:
                        print("Você é o ASSASSINO.")
                else:
                    print("ERRO")
            else:
                print("ERRO")
        else:
            print("ERRO")
    else:
        print("ERRO")    
else:
    print("ERRO")
