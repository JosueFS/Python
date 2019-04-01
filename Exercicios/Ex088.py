from random import randint
from time import sleep
apostas = []
jogo = []
print('-'*50)
print(f'{"JOGOS - MEGA SENA":^50}')
print('-'*50, end='\n')
qtJogos = int(input(f'Quantos jogos deseja gerar: '))
print('\n', '*'*15, f'SORTEANDO {qtJogos} JOGOS', '*'*15)

for c in range(0, qtJogos):
    for j in range(0,6):
        while (True):
            n = randint(1, 61)
            if n not in jogo:
                jogo.append(n)
                break
    jogo.sort()
    print(f'{c+1}° Jogo: {jogo}')
    sleep(1)
    apostas.append(jogo[:])
    jogo.clear()
print('='*19, 'BOA SORTE!', '='*19)
