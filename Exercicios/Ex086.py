matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o valor da posição [{l}, {c}]: ')))
for l in matriz:
    for c in l:
        print(f'[ {c} ]', end='')
    print()
