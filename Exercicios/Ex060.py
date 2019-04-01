from math import factorial
print(f'\n{" [ Calculando o Fatorial ] ":=^40}')
num = int(input('\nDigite um numero: '))
fat = 1
print(f'Calculando o fatorial de {num}! = ', end='')
while num > 0:
    fat *= num
    print(f'{num}', end='')
    print(f' x ' if num > 1 else f' = ', end='')
    num -= 1
print(f'{fat}.')