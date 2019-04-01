def contador(i, f, p):
    if i <= f:
        f+=1
    else:
        f-=1
        if p > 0:
            p = -p
    for c in range(i, f, p):
        print(c, end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(
    int(input(f'Inicio: ')),
    int(input(f'Fim: ')),
    int(input(f'Passo: '))
)
