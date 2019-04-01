valores = [str(input(f'Digite uma expressão: ')).strip()]
balores = []
for e in valores:
    for v in range(0, len(e)):
        balores.append(e[v])
print(f'{balores}')
print(f'{valores}')
print(balores.index(')'))
print(balores.index('('))
if balores.index(')') < balores.index('('):
    print(f'Expressão inválida.')
elif balores.count('(') == balores.count(')'):
    print(f'Expressão válida.')
else:
    print(f'Expressão inválida.')
