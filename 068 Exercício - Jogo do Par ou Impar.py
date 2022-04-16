''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
print("=" * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print("=" * 30)

#variaveis
vitoria = 0

while True:
    jogador_num = int(input("Digite um valor:"))
    tipo = ' '.upper()
    computador = randint(0, 10)
    soma = computador + jogador_num

    while tipo not in 'PpIi':
        tipo = str(input("Par ou Impar? [ P / I ]: "))
    if tipo == 'I':
        soma = computador + jogador_num
        if soma % 3 == 0:
            vitoria += 1
            print("_" * 30)
            print(f'Você jogou {jogador_num} e computador jogou {computador}. Total deu {soma}', end=" ")
            print("e é Par" if soma % 2 == 0 else 'e é Ímpar')
            print(f'Você GANHOU! Com o total de {vitoria} vitorias! Vamos jogar novamente!')
            print("_" * 30)
        else:
            break

    elif tipo == 'P':
        soma = computador + jogador2_num
        if soma % 2 == 0:
            vitoria += 1
            print("_" * 30)
            print(f'Você jogou {jogador_num} e computador jogou {computador}. Total deu {soma}',end=" ")
            print("e é Par" if soma % 2 == 0 else 'e é Ímpar')
            print(f'Você GANHOU! Com o total de {vitoria} vitorias! Vamos jogar novamente!')
            print("_" * 30)
        else:
            break

print("_" * 30)
print(f'Você jogou {jogador_num} e computador jogou {computador}. Total deu {soma}',end=" ")
print("e é Par" if soma % 2 == 0 else 'e é Ímpar')
print(f'Você perdeu! e teve {vitoria} vitoria(s)')
print("_" * 30)