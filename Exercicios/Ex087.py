matriz = [[],[],[]]
pares = 0
soma3 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o valor da posição [{l}, {c}]: ')))
for l in matriz:
    for c in l:
        print(f'[ {c} ]', end='')
        if c % 2 == 0:
            pares += c
    print()
    soma3 += l[2]
print('='*50)
print(f'Soma dos pares: {pares}')
print(f'Soma da 3° coluna: {soma3}')
print(f'Maior valor da 2° coluna: {max(matriz[1])}')