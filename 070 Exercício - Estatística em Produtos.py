'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

#variaveis
s = cont_1000 = menor_valor = nome = 0


print("=" * 40)
titulo = "Pichau. Comprei aqui a sua diversão"
print(titulo.center(60))
print("=" * 40)

while True:
    nome_produto = str(input("Nome do produto: "))
    n = float(input("Preço:R$"))
    s += n
    if n >= 1000:
        cont_1000 += 1
    if menor_valor == 0:
        menor_valor = n
        nome = nome_produto
    elif n < menor_valor:
        menor_valor = n
        nome = nome_produto
    quer_continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print("=" * 44)
print(f'O total gasto na compra foi de R$ {s:.2f}')
print(f'Temos {cont_1000} produto(s) que custam mais de R$1000')
print(f'O produto mais barato é {nome} custando {menor_valor}')
print("=" * 44)
