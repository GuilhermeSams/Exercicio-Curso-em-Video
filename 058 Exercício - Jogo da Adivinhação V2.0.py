'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.'''

print("Sou o seu computador...\nSerá se eu consigo adivinhar qual foi?")
from random import randint
computador = randint(0, 10)
cont_palpite = 0
jogador = int(input("Qual é o seu palpite? "))
while computador != jogador:
      if computador < jogador:
            print('MENOS... Tente mais uma vez')
      else:
            print("MAIS... Tente mais uma vez")
      jogador = int(input("Qual é o seu palpite? "))
      cont_palpite += 1
print(f'O computador jogou o número {computador} e o você jogou o número {jogador} PARABÉNS VOCÊ GANHOU!!!')
print(f'Foram feito(s) {cont_palpite} palpite(s)')
