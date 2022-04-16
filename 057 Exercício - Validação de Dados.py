''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = str(input("Informe o seu sexo: [M / F]: ")).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input("Dados inválidos, por favor Informe novamente o seu sexo: [M / F]: ")).upper()

if sexo == 'M':
    print("O sexo M é masculino")
elif sexo == 'F':
    print("O sexo F é feminino")
else:
    print("Entrada invalida")
