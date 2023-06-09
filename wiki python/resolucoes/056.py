"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
for i in range(n1 + 1, n2):
    print(i)
print("A soma dos numeros é: ", sum(range(n1 + 1, n2)))