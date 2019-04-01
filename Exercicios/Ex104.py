def leiaInt(n):
    while True:
        num = input(n)
        if not num.isnumeric():
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return num


print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
