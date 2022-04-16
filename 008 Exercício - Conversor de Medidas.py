'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

n1 = float(input("Digite um valor: "))
# 1 metro = 0,001 Km
# 1 metro = 0,01 hm
# 1 metro = 0,1 dam
# 1 metro = 10 dm
# 1 metro = 100 cm
# 1 metro = 1000 mm

km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print(f'{km}km\n{hm}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')