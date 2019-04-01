def maior(*num):
    print(f'Valores informados: ', end='')
    for c in num:
        print(c, end=' ')
    print(f'\nO maior valor é: {max(num)}')


maior(1,2,3)
maior(4,6,5,8,9,7,2)
