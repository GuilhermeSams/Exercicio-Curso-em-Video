'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''


import random

# ---------------Aqui nesse codigo tocado uma música--------------------
from pygame import mixer
mixer.init()
mixer.music.load('028 Exercício.mp3')
mixer.music.play()
#--------------------------------------------------------------------------------

computador = random.randint(1, 5)
print(81 * "*")
print('Estou pensando em um número! Qual será o número que eu estou pensado?')
print(81 * "*")

num_do_usuario = int(input("Em que número eu pensei? "))
if num_do_usuario == computador:
    print(f'Parabéns! O numero que eu pensei foi {computador} e você escolheu {num_do_usuario}')

else:
    print(f'Ganhei! Eu pensei no {computador} e você escolheu {num_do_usuario}')