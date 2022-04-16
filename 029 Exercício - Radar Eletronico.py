'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input("Velocidade do carro: "))
if velocidade <= 80:
    print('Tenha um ótimo dia. Dirija com segurança!')
else:
    print(f'Você foi multado, pois execeu o limite de velocidade que é de {velocidade:.0f}\nA multa será no valor de R$ {(velocidade - 80) * 7:.2f}!')