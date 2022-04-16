'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input())

unid = num // 1 % 10
dez = num // 10 % 10
cem = num // 100 % 10
milhar = num // 1000 % 10

print(f'Analisando um número {num}')
print(f'Unidade: {unid}')
print(f'Dezena: {dez}')
print(f'Centena: {cem}')
print(f'Milhar: {milhar}')
