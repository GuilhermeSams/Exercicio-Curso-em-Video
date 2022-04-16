'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
print('=' * 15)
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
print(" [ 1 ] somar")
print(' [ 2 ] multplicar')
print(' [ 3 ] maior')
print(' [ 4 ] trocar números')
print(' [ 5 ] sair do programa')
finalizar = False
while not finalizar:
    opcao = str(input("Qual é a sua opção: "))
    if opcao == '1':
        soma = num1 + num2
        print(f'A soma de {num1} + {num2} = {soma}')
        print('=' * 20)
    elif opcao == '2':
        mult = num1 * num2
        print(f'{num1} * {num2} = {mult}')
        print('=' * 20)
    elif opcao == '3':
        if num1 > num2:
            print(f'{num1} é maior')
            print('=' * 20)
        else:
            print(f'{num2} é maior')
            print('=' * 20)
    elif opcao == '4':
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
        print('=' * 20)
    elif opcao == '5':
        print('finalizando')
        finalizar = True
        print('='*20)
