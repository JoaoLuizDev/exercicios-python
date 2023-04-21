"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar:
  - M-matutino;
  - V-Vespertino; 
  - N- Noturno. 

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("Preciso saber em qual turno você estuda.\n  M- matutino;\n  V- vespertino;\n  N- noturno.\n")
turno = str(input("Digite a letra que corresponde ao seu turno:")).upper().strip()
if turno == "M":
  print("Bom dia.")
elif turno == "V":
  print("Boa tarde.")
elif turno == "N":
  print("Boa noite.")
else:
  print("Valor inválido.")
