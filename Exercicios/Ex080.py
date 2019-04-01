valores = []
while len(valores) < 5:
    novoValor = int(input(f'Digite um valor: '))
    if len(valores) == 0 or max(valores) <= novoValor:
        valores.append(novoValor)
        print(f'Adicionado no final da lista.')
    elif min(valores) >= novoValor:
        valores.insert(0, novoValor)
        print(f'Adicionado na posição 0 da lista.')
    else:
        for p, v in enumerate(valores):
            if valores[p] > novoValor and valores[p-1]  < novoValor:
                valores.insert(p, novoValor)
                print(f'Adicionado na posição {p} da lista.')
print(f'Lista de valores: {valores}')
