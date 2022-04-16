'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
sexo = int(input('''Digite seu sexo: 
[ 1 ] masculino
[ 2 ] feminino
Opçaõ: '''))

if sexo == 1:
    ano = int(input("Ano de Nascimento: "))
    ano_atual = date.today().year
    calc_qnt_anos_faltam = (abs(ano - ano_atual))
    calc_qnd_era_alistamento = (calc_qnt_anos_faltam - 18)

    print(f'Quem nasceu em {ano} tem {abs(calc_qnt_anos_faltam)} em {ano_atual}')
    if calc_qnt_anos_faltam == 18:
        print("Você tem que se alistar imediatamente")

    elif calc_qnt_anos_faltam > 18:
        print(f' Já se passaram {calc_qnt_anos_faltam - 18} anos. Você tem que se apresentar em uma Junta de Serviço Militar urgente!\n Seu alistamento foi em {ano_atual - calc_qnd_era_alistamento}')

    elif calc_qnt_anos_faltam < 18:
        print(f'Ainda faltam {18 - calc_qnt_anos_faltam}  anos para se alistar')
        print(f'Seu alistamento será {ano_atual - calc_qnd_era_alistamento}')

elif sexo == 2:
    print("Você não precisa se alistar")