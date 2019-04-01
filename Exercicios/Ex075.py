#Pegando os valores e Armazenando na tupla
numeros = (int(input(f'Digite o 1° número: ')), int(input(f'Digite o 2° número: ')),
           int(input(f'Digite o 3° número: ')), int(input(f'Digite o 4° número: ')))
print('='*30)
print(f'Os números digitados são {numeros}')
print('='*30)
if 9 in numeros:
    print(f'O número 9 aparece {numeros.count(9)} vez(es).')
else:
    print(f'O número 9 não aparece na tupla.')
print('='*30)
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}° posição,')
else:
    print(f'O número 3 não aparece na tupla.')
print('='*30)
a = False
print(f'Os números par(es) são ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'{c} ', end='')
        a = True
if a == False:
    print(f'(Vazio).')
