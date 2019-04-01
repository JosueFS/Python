n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print(f'Os segmentos informados formam um triângulo!')
else:
    print(f'Os segmentos não formam um triângulo.')
