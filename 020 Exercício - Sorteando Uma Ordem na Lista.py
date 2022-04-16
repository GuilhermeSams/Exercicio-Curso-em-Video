from random import  shuffle
nome1 = input("Nome do aluno: ")
nome2 = input("Nome do aluno: ")
nome3 = input("Nome do aluno: ")
nome4 = input("Nome do aluno: ")

lista =  [nome1, nome2, nome3, nome4]
shuffle(lista)

print(f'A ordem  da apresentação será {lista}')