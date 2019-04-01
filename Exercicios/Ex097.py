def escreva(msg):
    tam = len(msg)+2
    print('-'*tam)
    print(f'{f"{msg}": ^{tam}}')
    print('-' * tam)


texto = str(input(f'Digite uma mensagem: '))
escreva(texto)