''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

r1 = float(input("Coloque o valor de um lado: "))
r2 = float(input("Coloque o valor do outro lado: "))
r3 = float(input("Coloque o valor do outro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triangulo!")
else:
    print("Não é possível formar um triangulo!")


