produtos = ('Placa de Video EVGA Gtx 960', 1440,
            'Processador Core i5-4440', 849,
            '2x8GB HyperX Fury DDR3 1600Mhz', 750,
            'Seagate Barracuda 2TB', 200)
print('-'*50)
print(f'{"[ MEU PC ]":^50}')
print('-'*50)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print('{:.<40}'.format(produtos[p]),end='')
    else:
        print(f'R${produtos[p]:>4},00')
print('-' * 50)