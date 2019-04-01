a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print(f'Os segmentos podem formar um triângulo EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print(f'Os segmentos podem formar um triângulo ISÓSCELES.')
    else:
        print(f'Os segmentos podem formar um triângulo ESCALENO.')
else:
    print(f'Os segmentos não formam um triângulo.')
