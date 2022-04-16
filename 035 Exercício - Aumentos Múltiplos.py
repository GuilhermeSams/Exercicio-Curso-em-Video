'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

valor = float(input("Digite o salário do funcionário: "))

if valor <= 1250.00:
    novo = valor + (valor * 15 / 100)
else:
    novo = valor + (valor * 10 / 100)

print(f'Quem ganhava R$ {valor:.2f} passa a ganhar R$ {novo:.2f}')