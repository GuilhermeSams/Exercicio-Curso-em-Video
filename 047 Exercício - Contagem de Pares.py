'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

for cont in range(2, 50+1, 2):
    if cont % 2 == 0:
        print(cont, end=" | ")