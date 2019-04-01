print(f'='*30)
print(f'{"10 TERMOS DE UMA PA": ^30}')
print(f'='*30)
n1 = int(input(f'Primeiro termo: '))
inc = int(input(f'Razão: '))
max = n1 + (10 - 1) * inc + inc
for cont in range(n1, max, inc):
    print(f' {cont} →', end='')
print(f' ACABOU')
