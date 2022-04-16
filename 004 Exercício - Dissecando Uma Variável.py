'''Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre
 na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''


n = (input("Digite um numero:"))

print(type(n))

print (f"É um numero? {n.isnumeric()}")
print (f'é um alfa numero? {n.isalnum()}')
print (f'São letras? {n.isalpha()}')
print (f'Tem espaço? {n.isspace()}')