'''Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado')

elif media >= 5 or media <6.9:
    print("Recuperação!")

elif media >= 7:
    print("Aprovado!")