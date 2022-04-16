'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

lista_idade = []
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
cont_mulher = 0

for a in range(1, 5):
    print(f'-------- {a}ª PESSOA --------')
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M / F]: ")).upper()
    lista_idade += [idade]
    media_idade = sum(lista_idade)
    if a == 1 and sexo == "Mn":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Mn" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == "F":
        if idade < 20 and sexo in "Ff":
            cont_mulher += 1

print(f'A média de idade do grupo é de {media_idade / 4} anos')
print(f'O homem mais velho tem {maior_idade_homem} e e se chama {nome_velho}')
print(f'Ao todo são {cont_mulher} com menos de 20 anos')

