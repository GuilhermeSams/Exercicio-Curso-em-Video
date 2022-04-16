'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input("Digite um valor inteiro: "))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao= int(input("Digite uma opção: "))

if opcao == 1:
    print(f'{num} convertido para BINÀRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} Convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convertido para HEXADECIMAL {hex(num)[2:]}')
else:
    print("Você digitou  uma opção invalida! Por favor verifique a entrada e digite novamente!")

