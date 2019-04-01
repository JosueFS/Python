opt = 4
n1 = 0
n2 = 0
while True:
    if opt == 1:
        print(f'\nA soma entre {n1} + {n2} é {n1+n2}.')
    elif opt == 2:
        print(f'\nO resultado de {n1} x {n2} é {n1*n2}.')
    elif opt == 3:
        print(f'\nEntre {n1} e {n2} o maior valor é {max(n1,n2)}.')
    elif opt == 4:
        print('=' * 25)
        print(f'[ Informe os números ]')
        n1 = int(input(f'Primeiro valor: '))
        n2 = int(input(f'Segundo valor: '))
    elif opt == 5:
        input(f'Finalizando...')
        break
    else:
        print('Opção inválida.')
    print('=' * 25)
    print('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Valores\n[ 5 ] Sair')
    opt = int(input(f'\nEscolha a opção: '))
