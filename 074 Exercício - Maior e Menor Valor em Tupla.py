'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint

gerador = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print("Os valores sorteados foram: ", end=" ")
for c in gerador:
    print(f'{c}', end=" ")

print(f'\nO maior valor sorteado foi: {max(gerador)}')
print(f'O menor valor sorteado foi: {min(gerador)}')