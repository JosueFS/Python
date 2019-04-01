valores = []
while True:
    onOff = 'a'
    novoValor = int(input(f'Digite um valor: '))
    if novoValor in valores:
        print(f'Valor duplicado. Valor não será adicionado.')
    else:
        valores.append(novoValor)
        print(f'Valor adicionado com Sucesso!')
    print('-' * 40)
    while onOff not in 'SsNn':
        onOff = str(input(f'Deseja continuar? [S / N]')).strip()
    if onOff in 'nN':
            break
    print('-' * 40)
valores.sort()
print(f'='*40)
print(f'Valores digitados: {valores}')
print(f'='*40)
print(len(valores))