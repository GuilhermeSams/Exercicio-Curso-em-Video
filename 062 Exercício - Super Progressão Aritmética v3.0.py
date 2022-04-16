'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro_termo = int(input("Primeiro termo: "))
razao_PA = int(input("Razão da PA: "))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(primeiro_termo, end="→")
        primeiro_termo += razao_PA
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar? "))
print(f'Progressão finalizada com {total} termos mostrados.')


