'''palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')



for txt in palavras:
    print(f'Na palavra {txt.upper()} temos ', end=" ")
    for letra in txt:
        if letra.lower() in vogais:
            print(f'{letra}', end=" ")
    print()'''

aluno = ['123', 'fulano de tal','20','EE',1.5]
sicrano = ['124','sicrano de tal','18','EE',1.6]
beltrano = ['1','beltrano da silva', '50','EE', 1.7]
x = ['12','beltrano da silva', '50','EE', 1.7]
turma = [aluno, sicrano, beltrano]

for ord_aluno in turma[1]:
    turma.sort
    print(turma)