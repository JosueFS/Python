valores = list()
while True:
    onOff = 'a'
    novoValor = int(input(f'Digite um valor: '))
    valores.append(novoValor)
    print(f'Valor adicionado com Sucesso!')
    print('-' * 40)
    while onOff not in 'SsNn':
        onOff = str(input(f'Deseja continuar? [S / N]')).strip()
    if onOff in 'nN':
        print('=' * 40)
        break
    print('-' * 40)
print(f'Lista de valores: {valores}')
print('-' * 40)
#Analisando numeros pares e impares
pares = []
impares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
#Exibindo novas listas
print(f'Lista de pares: {pares}')
print('-' * 40)
print(f'Lista de impares: {impares}')
print('=' * 40)