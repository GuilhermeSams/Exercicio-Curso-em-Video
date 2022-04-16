from  time import sleep
from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input("Qual a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
print("=*" * 13)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogada]}')
print("=*" * 13)

if computador ==0: # computador jogou pedra
    if jogada ==0:
        print("Jogo empatado")
    elif jogada ==1:
        print("Jogador ganhou")
    elif jogada == 2:
        print("Computador ganhou")
    else:
        print("Opção invalida! Por favor verifique a entrada e digite novamente.")

elif computador ==1: # computador jogou papel
    if jogada == 0: #pedra
        print("computador ganhou")
    elif jogada == 1:#papel
        print("Empate")
    elif jogada ==2:#tesoura
        print("Jogador ganhou")
    else:
        print("Opção invalida! Por favor verifique a entrada e digite novamente.")

elif computador ==2: # computador jogou tesoura
    if jogada == 0: #pedra
        print("Computador ganhou")
    elif jogada ==1: #papel
        print("Computador ganhou")
    elif jogada ==2:
        print("Empate")
    else:
        print("Opção invalida! Por favor verifique a entrada e digite novamente.")