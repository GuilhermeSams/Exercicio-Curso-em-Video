'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''


print("=" * 30)
print("Banco SAMS".center(60))
print("=" * 30)

#entrada
valor = int(input("Que valor você quer sacar? R$"))

#computação com saída
calc_50 = valor  // 50
valor %= 50

calc_20 = valor // 20
valor %= 20

calc_10 = valor // 10
valor %= 10

calc_1 = valor // 10
valor %= 10

if calc_50 > 0:
    print(f'Total de {calc_50} cédulas de R$ 50')

if calc_20 > 0:
    print(f'Total de {calc_20} cédulas de R$ 20')

if calc_10 > 0:
    print(f'Total de {calc_10} cédulas de R$ 10')

if calc_1 > 0:
    print(f'Total de {calc_1} cédulas de R$ 1')