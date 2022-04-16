'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''


n = ("Zero","Um", "Dois", "Tres","Quatro", "Cinco","Seis", "Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quartorze",
                  "Quinze", "Dezeseis","Dezesete","Dezoito","Dezenove","Vinte")

while True:
    while True:
        pos = int(input("Digite um número entre 0 e 20: "))
        if 0 <= pos <= 20:
            break
        print(f'Número invalido', end=" ")
    print(f'{n[pos]}')
    print(' ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break






