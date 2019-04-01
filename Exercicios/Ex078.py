valores = []
for c in range(5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))
print(f'='*40)
print(f'Lista de valores: {valores}')
print(f'='*40)
print(f'Maior numero: {max(valores)}')
print(f'Posição:', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f' [{p}]', end='')
print(f'\n' + '-'*40)
print(f'Menor numero: {min(valores)}')
print(f'Posição:', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f' [{p}]', end='')
print(f'\n' + '='*40)
