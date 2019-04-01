def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {int(gols)} gols'


n = str(input(f'Nome: '))
g = str(input(f'Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
    