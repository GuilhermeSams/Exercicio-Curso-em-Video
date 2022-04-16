'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

n1 = float(input("Digite um valor: R$"))
desc = int(input("Digite um desconto: "))

novo_salario = n1 * desc / 100
calc_novo_salario = n1 + novo_salario

print(f'O salario desse funcionario é de R${n1} e com 15% de aumento passará a ter R${calc_novo_salario:.2f}')
