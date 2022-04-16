'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
cont = 0

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

tupla = (n1, n2, n3, n4)
print("Você digitou os valores", end=" ")
for i in tupla:
    print(i, end=" ")

print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f"O valor 3 foi digitado na posição {tupla.index(3)+1}")
else:
    print("O valor 3 não foi digitado em nenhuma posição")

for c in tupla:
    if c % 2 == 0:
        cont += 1
    if cont == 0:
        print("Nenhum valor par foi digitado")
    else:
        print("Os valores pares digitados foram: ",end=" ")
        for p in tupla:
            if p % 2 == 0:
                print(f'{p}', end="")
            break
