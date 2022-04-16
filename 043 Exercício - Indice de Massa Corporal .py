''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso y6tg
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input("Digite seu peso em Kg : "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print(f'O IMC desta pessoa é de {imc:.1f}')

if imc < 18.5:
    print("ABAIXO DO PESO! Se for ao caso extremo, por favor consulte um nutricionista")
elif imc < 25:
    print("Que ótimo! Você está no PESO IDEAL!")
elif imc < 30:
    print("SOBREPESO! Se haver histórico de problemas familiar fique atento!")
elif imc < 40:
    print("OBESIDADE, fique atento aos probelmas de saúde!")
else:
    print("OBESIDADE MORBIDA, consulte um expecialista ugente!")