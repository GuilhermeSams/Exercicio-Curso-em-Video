''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0 # esse num recebe zero é uma gambiarra para que o while possa ler  a entrada, caso contrario apresentara error
cont = 0  #  esse soma também recebe 0 porque não foi lido nenhum número
soma = 0 # esse soma também recebe 0 porque não foi lido nenhum número

num = int(input("Digite um número [999 para parar]: "))
while num != 999: # flag
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f' Você digitou {cont} números e a soma entre é {soma}.')