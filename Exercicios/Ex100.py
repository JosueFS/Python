from random import randint
def sorteia(lista):
    for c in range(0,5):
        lista.append(randint(0,9))
    print(f'Números sorteados: {lista}')
def somaPar(lista):
    a = 0
    for e in lista:
        if e % 2 == 0:
            a += e
    print(f'Soma dos Pares: {a}')


numeros = []

sorteia(numeros)
somaPar(numeros)
