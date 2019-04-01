# n[0] pares // n[1] impares
n = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° valor: '))
    if num % 2 == 0:
        n[0].append(num)
    else:
        n[1].append(num)
n[0].sort()
n[1].sort()
print('=' * 50)
print(f'Os números pares digitados foram: {n[0]}')
print(f'Os números impares digitados foram: {n[1]}')
