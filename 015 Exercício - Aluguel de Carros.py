dia = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

calc_dia = dia * 60
cal_km = km * 0.15

print(f'O valor a pagar é de R${calc_dia + cal_km:.2f}')








'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''