'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

print("-"*36)
print('Sequência Fibonacci')
print("-"*36)
cont_a = 0
cont_b = 1
cont = 3
N = int(input("Quantos termos você quer mostrar? "))


print('~'*36)
print(f'{cont_a} → {cont_b}', end=" ")

while cont <= N:
    cont_c = cont_a + cont_b
    print(f'→ {cont_c}', end=" ")
    cont_a = cont_b
    cont_b = cont_c
    cont += 1
print("Fim")
