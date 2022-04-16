'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''


num = int(input("Digite um valor: "))

print(f' O dobro de {num} é {num*2}, seu triplo {num*3} e sua raiz quadrada {pow(num,(1/2))}')

'''
O codigo também pode ser descrito da seguinte maneira
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5

print(f' O dobro de é {dobro}\n seu tripo é {triplo}\n e a sua raiz quadrada é {raiz_quadrada:.0f}')
'''

