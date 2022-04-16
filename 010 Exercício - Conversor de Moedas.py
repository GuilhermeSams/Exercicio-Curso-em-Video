real = float(input('Quanto dinheiro você tem na carteira? R$ '))


#US$ 1,00 = 0.18 cents
#R$ 1,00 = R$ 5.46
#Euro 1,00 =  R$ 6.25
#Libra 1.00 = R$ 0.14

print(f'{real / 6.25:.2f} Euro')
print(f'{real / 5.46:.2f} Dolar')
