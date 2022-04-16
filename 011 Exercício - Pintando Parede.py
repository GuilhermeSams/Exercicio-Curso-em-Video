'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua áreae a quantidade de
tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

calc = largura * altura

pintura = calc / 3

print(f'A parede tem {calc}m²')
print(f'Para pintar a parede será necessário(s) {pintura}l de tinta. ')
