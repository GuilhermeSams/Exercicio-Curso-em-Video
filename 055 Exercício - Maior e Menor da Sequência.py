'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
lista = []
for pess in range(0, 5):
    peso = float(input("Peso da pessoa: "))
    lista += [peso]
print(f'O maior valor peso lido foi de {max(lista)}Kg')
print(f'O menor valor peso lido foi de {min(lista)}Kg')