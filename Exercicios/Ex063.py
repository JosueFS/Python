print(f'-'*30)
print(f'{"[ Sequência de Fibonacci ]": ^30}')
print(f'-'*30)
termos = int(input(f'Quantos termos você quer mostrar? '))
ant = 1
fib = 0
print(f'~'*30)
while termos != 0:
    print(f'{fib}', end=' → ')
    fib = fib + ant
    ant = fib - ant
    termos -= 1
print(f'FIM')
print(f'~'*30)
