from random import randint
jogador = {}
gols = []
jogador['nome'] = str(input(f'Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, partidas):
    #gols.append(int(input(f'Gols na {g+1}° Partida: ')))
    gols.append(randint(0,4)) #Quantidade aleatória de gols
jogador['gols'] = gols[:]
jogador['Total'] = sum(gols)
print('='*50)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('='*50)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for i, a in enumerate(jogador['gols']):
    print(' '*5, f'=> Na {i+1}° Partida, fez {a} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
print('='*50)
