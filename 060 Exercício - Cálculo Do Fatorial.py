'''Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
'''
from math import factorial
num = int(input("Digite um valor: "))
f = factorial(num)
print(f)
'''

num = int(input("Digite um valor: "))
c = num
f = 1
print(f'Calculando {num}! = ',end=" ")
while c > 0:
    print(f'{c}', end=" ")
    print(' x ' if c > 1 else ' =', end=" ")
    f *= c
    c -= 1
print(f'{f}')

############## fazer com for #################