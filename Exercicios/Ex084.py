pessoas = list()
pessoa = list()
while (True):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    if len(pessoas) == 1:
        ma = me = pessoa[1]
    if pessoa[1] > ma:
        ma = pessoa[1]
    if pessoa[1] < me:
        me = pessoa[1]
    pessoa.clear()
    opt = str(input(f'\nDeseja Continuar [S/N]?'))
    if opt in 'Nn':
        break

print(f'\nPessoas cadastradas: {len(pessoas)}')
print(f'Maior peso: {ma:.1f}Kg. Peso de', end=' ')
for a in pessoas:
    if a[1] == ma:
        print(f'[{a[0]}]', end=' ')
print(f'\nMenor peso: {me:.1f}Kg. Peso de', end=' ')
for b in pessoas:
    if b[1] == me:
        print(f'[{b[0]}]', end=' ')
