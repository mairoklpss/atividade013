# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.
nm = int(input("digite um número: "))

# Informar em que categoria o número se enquadra.
if nm < 0:
    print (f"o número {nm} é negativo.")
elif nm == 0:
    print (f"o número {nm} é zero.")
else:
    print (f"o número {nm} é positivo.")