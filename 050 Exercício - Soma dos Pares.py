''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
cont = 0
cont_par = 0
for c in range(0, 6):
    num = int(input("Digite um número inteiro: "))
    cont += 1
    if num % 2 == 0:
        soma += num
        cont_par = cont_par + 1
print(f' Foram {cont} números, dentre eles {cont_par} números são pares e a soma de todos números pares é {soma}')
