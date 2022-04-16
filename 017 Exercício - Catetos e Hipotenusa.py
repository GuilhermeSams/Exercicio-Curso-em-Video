'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa'''
from math import hypot, sqrt
comp_cateto_oposto = float(input("Dgite um valor: "))
comp_cateto_odjacente = float(input("digite um valor: "))
hi = hypot(comp_cateto_oposto, comp_cateto_odjacente)
print(f'A hipotenusa vai medir {hi:.2f}')



'''
O calculo também pode ser descrito da seginte forma

a = comp_cateto_oposto ** 2 + comp_cateto_odjacente ** 2

calc = sqrt(a)

print(f'A hipotenusa vai medir {calc:.2f}')

'''

