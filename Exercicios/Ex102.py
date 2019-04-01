def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param num: O numero a ser calculado.
    :param show: (Opcional) Se True, mostra o calculo.
    :return: Retorna o fatorial de num.
    """
    t = 1
    for c in range(num, 0, -1):
        t *= c
        if (show):
            print(f'{c} ', end='')
            if c == 1:
                print(f'=', end=' ')
            else:
                print(f'x ', end='')
    return t


print(fatorial(10, False))
help(fatorial)
