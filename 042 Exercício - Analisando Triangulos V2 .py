'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

r1 = float(input("Coloque o valor de um lado: "))
r2 = float(input("Coloque o valor do outro lado: "))
r3 = float(input("Coloque o valor do outro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILATERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
    elif r1 != r2 or r1 != r3 or r2 != r3:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
else:
    print("Não é possível formar um triangulo!")