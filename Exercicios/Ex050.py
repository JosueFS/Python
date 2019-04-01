num = 0
soma = 0
for cont in range(0, 6):
    num = int(input(f'Digite o {cont+1}° número: '))
    if num % 2 == 0:
        soma += num
print(f'Soma: {soma}')