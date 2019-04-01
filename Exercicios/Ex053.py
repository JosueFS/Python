abc = str(input(f'Digite uma frase: ')).strip().upper().split()
abc = ''.join(abc)
inv = ''
for letra in range(len(abc)-1, -1, -1):
    inv += abc[letra]
print(f'O inverso de {abc} é {inv}.')
if abc == inv:
    print(f'É PALÍNDROMO')
else:
    print(f'NÃO É PALÍNDROMO')
