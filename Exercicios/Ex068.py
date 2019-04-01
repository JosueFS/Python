from random import randint
v = 0
while True:
    opt = ' '
    while opt not in 'PI':
        opt = str(input(f'Escolha Par ou Impar [ P / I ]: ')).strip().upper()
    num = int(input(f'Escolha um número: '))
    print(f'='*40)
    print(f'Verificando..')
    print(f'='*40)
    pc = randint(0,9)
    if (num + pc) % 2 == 0:
        if opt == 'P':
            print(f'{num+pc} é Par')
            print(f'Parabéns, você venceu!')
            v += 1
        if opt == 'I':
            print(f'{num + pc} é Par')
            break
    else:
        if opt == 'P':
            print(f'{num+pc} é Impar')
            break
        if opt == 'I':
            print(f'{num + pc} é Impar')
            print(f'Parabéns, você venceu!')
            v += 1
print(f'Infelizmente, você perdeu.')
print(f'Você conseguiu {v} Vitória(s)!')