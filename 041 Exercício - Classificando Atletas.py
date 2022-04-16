'''A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date
ano = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = abs(ano - ano_atual)
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print("MIRIM")
elif idade >= 10 and idade <= 14:
    print("INFANTIL")
elif idade >= 15 and idade <= 19:
    print("JUNIOR")
elif idade == 20:
    print("SÊNIOR")
elif idade > 20:
    print("MASTER")