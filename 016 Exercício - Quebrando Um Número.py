'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import floor
num = float(input("Digite um valor: "))

print(f'O valor digitado foi {num} e sua posição interira é {(num.__floor__())}')