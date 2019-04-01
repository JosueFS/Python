while True:
    print(f'-' * 30)
    num = int(input(f'Informe o valor da tabuada: '))
    print(f'-' * 30)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c:2} = {num * c}')
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
