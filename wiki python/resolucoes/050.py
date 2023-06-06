"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
"""

while True:
    pais_a = int(input("Digite o número de habitantes do país A: ")) #população país A
    while pais_a < 0:                                           
        print("Dado inválido. Tente novamente.")
        pais_a = int(input("Digite o número de habitantes do país A: "))
    pais_b = int(input("Digite o número de habitantes do país B: ")) #população país B
    while pais_b < 0:
        print("Dado inválido. Tente novamente.")
        pais_b = int(input("Digite o número de habitantes do país B: "))
    taxa_a = float(input("Digite a taxa percentual de crescimento anual do país A: "))
    while taxa_a < 0:
        print("Dado inválido. Tente novamente.")
        taxa_a = float(input("Digite a taxa percentual de crescimento anual do país A: "))
    taxa_b = float(input("Digite a taxa percentual de crescimento anual do país B: "))
    while taxa_b < 0:
        print("Dado inválido. Tente novamente.")
        taxa_b = float(input("Digite a taxa percentual de crescimento anual do país B: "))
    anos = 0

    if pais_a > pais_b:
        print("País A já é maior que país B.")
    else:
        if taxa_a < taxa_b:
            print("O país A nunca será mais populoso que o país B.")
        else:
            while pais_a < pais_b:
                pais_a += pais_a * (taxa_a / 100)
                pais_b += pais_b * (taxa_b / 100)
                anos += 1

            print(f"Em {anos} anos, o país A ultrapassará o país B.")

    opcao = input("Deseja realizar outra operação? (s/n): ")
    if opcao.lower() != 's':
        break