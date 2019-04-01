palavras = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
for p in palavras:
    print(f'\nNa palavra {str(p).upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra}', end='')
