print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 0

while cont <= 10:
    print(primeiro_termo, end="→")
    primeiro_termo += razao
    cont += 1
print("Fim")

