num = int(input(f'Digite um numero: '))
tot = 0
for cont in range(1, num+1):
    if (num % cont) == 0:
        print(f'\033[1;33m{cont} ', end=' ')
        tot += 1
    else:
        print(f'\033[1;31m{cont} ', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vez(es)')
if tot == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')
