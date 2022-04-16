'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
#variaveis
cont_mais_18 = 0
cont_sexo_M = 0
cont_sexo_F_20 = 0
#inicio
titulo = 'CADRASTRE UMA PESSOA'
print("=" * 30)
print(titulo.center(30))
print("=" * 30)
#estrutura de repetição infinita
while True:
    idade = int(input("Idade: "))
    Sexo = str(input("Sexo: [M/F] ")).upper()
    quer_continuar = str(input("Quer continuar? [S/N] "))
    titulo = 'CADRASTRE UMA PESSOA'
    print("=" * 30)
    print(titulo.center(30))
    print("=" * 30)
    print("#" * 100)
#condições
    if idade >= 18:
        cont_mais_18 += 1
    if Sexo == 'M':
        cont_sexo_M += 1
    if Sexo == 'F':
        if idade <= 20:
            cont_sexo_F_20 += 1
#se o usuario digitar "N" o programa sará interrompindo e ocorrerá a saída esperada
    if quer_continuar == 'N':
        break
print(f' Total de pessoas com mais de 18 anos: {cont_mais_18}')
print(f'Ao todo temos {cont_sexo_M} homem (ns) cadrastrados')
print(f'E temos {cont_sexo_F_20} mulher (es) com menos de 20 anos')