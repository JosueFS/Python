valores = []
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
print(f'A Lista contém {len(valores)} valores.')
print('-' * 40)
valores.sort(reverse=True)
print(f'Valores em Ordem Descrescente: {valores}')
print('-' * 40)
if  5 in valores:
    print(f'O valor 5 foi digitado.')
else:
    print(f'O Valor 5 não foi encontrado na lista.')
print('-' * 40)