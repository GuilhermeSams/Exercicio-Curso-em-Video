'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print(f'{"Lojas GuiSams":=^40}')
preco = float(input("Digite o preço das compras: R$ "))

opcao = int(input(   '''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if opcao == 1:
    desconto_dinheiro = (preco * 10) / 100
    preco_desconto_dinheiro = preco - desconto_dinheiro
    print(f'Você está pagando a vista no dinheiro ou cheque, então o preço que estava R$ {preco:.2f} será de R$ {preco_desconto_dinheiro:.2f}')

elif opcao == 2:
    desconto_cartao = (preco * 5) / 100
    preco_desconto_cartao = preco - desconto_cartao
    print(f'Você está pagando a vista no cartão, então o preço que estava R$ {preco:.2f} será de R$ {preco_desconto_cartao:.2f}')

elif opcao == 3:
    parcela_duas = preco / 2
    print(f'Sua compra será parcelada em 2x ficará de R$ {parcela_duas:.2f}')
    print(f'Você está pagando em 2x cartão, então o preço será sem desconto')
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco} no final ')

elif opcao == 4:
    parcela = int(input("Quantas parcelas? "))
    juros = (preco * 1.20)
    print(f'Sua compra será parcela em {parcela}x de R$ {juros / parcela:.2f} com JUROS')
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {juros:.2f} no final ')

else:
    print(f'Forma de pagamento invalida! Por favor, verifique a forma de pagamento.')








