from time import sleep
from random import randint
from operator import itemgetter
jogadores = {}
#asc = []
jogo = {}
print(f'Valores sorteados: ')
for n in range(0,4):
    num = randint(1,6)
    print(' '*5, f'jogador{n+1}: {num}')
    jogadores[f'jogador{n+1}'] = num
    sleep(1)
# for v in jogadores.values():
#     asc.append(v)
# asc.sort(reverse=True)
jogo = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'Ranking dos jogadores: ')
# for c in range(0, len(jogadores)):
#     for k, v in jogadores.items():
#         if v == asc[c]:
#             print(' '*5, f'{c+1}° Lugar: {k} - {v}')
#             jogadores.pop(k)
#             break
for i, v in enumerate(jogo):
    print(f'   {i+1}° Lugar: {v[0]} - {v[1]}.')