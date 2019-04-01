print(f'='*30)
print(f'{"10 TERMOS DE UMA PA": ^30}')
print(f'='*30)
n1 = int(input(f'Primeiro termo: '))
inc = int(input(f'Razão: '))
cont = 0
while cont < 10:
    print(f'{n1} → ', end='')
    n1 += inc
    cont += 1

print(f'FIM')