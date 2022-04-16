'''Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.'''
angulo = int(input("Digite o angulo: "))

import math

calc_seno = math.sin(math.radians(angulo))
calc_cosseno = math.cos(math.radians(angulo))
calc_tangente = math.tan(math.radians(angulo))

print(f'O angulo de {angulo} tem o SENO {calc_seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO {calc_cosseno:.2f}')
print(f'O angulo de {angulo} tem a TANGENTE {calc_tangente:.2f}')