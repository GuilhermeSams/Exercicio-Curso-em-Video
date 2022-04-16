'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ("Atletico - MG","Flamengo","Palmeiras","Fortaleza","Corinthians",
         "Bagrantino","Fluminense","America - MG","Atletico Goianiense","Santos",
         "Ceara","Internacional","Sao Paulo","Athletico - PR","Cuiaba",
         "Juventude","Gremio","Bahia","Sport","Chapecoense")

'''for t in times:
    print(f'{t}',end=" | ")'''


print("="*30)
print(f'Lista de times do Brasilieirão: {times}')
print("="*30)
print(f'Os 5 primeiros times são: {times[0:5]}')
print("="*30)
print(f'{times[-4:]}')
print("="*30)
print(f'O times em ordem alfabetica é: {sorted(times)}')
print("="*30)
print(f'A posição do Chapecoense é: {times.index("Chapecoense")+1}º')