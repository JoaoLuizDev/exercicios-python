"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

print("Informe seu sexo: \n"
      "M - Masculino\n"
      "F - Feminino")
sexo = str(input("Informe a opção: "))
if genero == M:
  print("Sexo Masculino.")
elif genero == F:
  print("Sexo Feminino.")
else:
  print("Sexo inválido.")

#na resolução abaixo, usei as funções .strip e .upper
# s.trip para remover os espaços em branco do início e do fim da string
# .upper para converter a string para maiúsculas

 print("Informe seu sexo: \n"
      "M - Masculino\n"
      "F - Feminino")
sexo = str(input("Informe a opção: ")).strip().upper()
if genero == M:
  print("Sexo Masculino.")
elif genero == F:
  print("Sexo Feminino.")
else:
  print("Sexo inválido.")
