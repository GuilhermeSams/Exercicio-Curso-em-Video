'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''


n1 = float(input("Digite um valor: "))

desconto = (n1 * 10) / 100
calc = n1 - desconto

print(f'O preço deste protudo custa {n1:.2f} e com desconto de 5% ficará {calc:.2f}')