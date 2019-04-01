print(f'='*30)
print(f'{"10 TERMOS DE UMA PA": ^30}')
print(f'='*30)
n1 = int(input(f'Primeiro termo: '))
inc = int(input(f'Razão: '))
qt = 0
cont = 10
while qt < cont:
    print(f'{n1} → ', end='')
    n1 += inc
    if qt == (cont-1):
        print(f'PAUSA')
        cont = int(input(f'Mais quantos termos deseja exibir? ')) + qt +1
    qt += 1
print(f'Progressão finalizada com {qt} termos exibidos.')