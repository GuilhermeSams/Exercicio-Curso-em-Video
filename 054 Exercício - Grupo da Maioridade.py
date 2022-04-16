'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
cont_maior_de_idade = 0
cont_menor_de_idade = 0

for c in range(1, 8):
    ano = int(input("Em que ano a pessoa nasceu? "))
    ano_atual = date.today().year
    calc_anos = ano_atual - ano
    if calc_anos >= 18:
        cont_maior_de_idade += 1
    if calc_anos < 18:
            cont_menor_de_idade += 1

print(f'Ao todo tivemos {cont_maior_de_idade} pessoas maiores de idade')
print(f'E também tivemos {cont_menor_de_idade} pessoas menores de idade')







