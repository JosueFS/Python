numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input(f'Digite um número entre 0 e 20: '))
    if num in range(0, len(numeros)):
        break
    print(f'Tente novamente.',end=' ')
print(f'Você digitou o número {numeros[num]}!')
