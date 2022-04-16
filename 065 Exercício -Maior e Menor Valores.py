'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''



cond = 'S'
cont = 0
soma = 0
lista = []
while cond == 'S':
    num = (int(input("Digite um número: ")))
    cond = str(input("Quer continuar [S / N] ? ")).upper()
    cont += 1
    soma += num
    lista += [num]

print(f' Você digitou {cont} e a média foi {soma / cont}')
print(f' O maior valor foi {max(lista)} e o menor valor foi {min(lista)}')
