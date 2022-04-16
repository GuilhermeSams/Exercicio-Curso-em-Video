'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print("="*50)
print("LISTAGEM DE PREÇOS".center(100))
print("="*50)

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)

for p in range(0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:.<30}', end="")
    else:
        print(f'R${listagem[p]:>7.2f}')

print("="*50)