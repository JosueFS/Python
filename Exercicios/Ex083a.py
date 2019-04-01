expr = str(input(f'Digite a expressão: '))
pilha = []
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Valida')
else:
    print(f'Invalida')