'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Salário do Comprador: "))
ano_financiamento = int(input("Quantos anos de financiamento? "))

prestacao = valor_casa / (ano_financiamento * 12)

print(f'Para pegar uma casa no valor de {valor_casa:.2f} em {ano_financiamento} anos a prestação será de R${prestacao:.2f}')

if prestacao > (salario_comprador * 0.3):
    print("Prestação NEGADA!")
else:
    print("Prestaçaõ APROVADA!")