soma = qtd = 0
while True:
    num = int(input(f'Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qtd += 1
print(f'Você digitou {qtd} números e a soma entre eles foi {soma}.')
