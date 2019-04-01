soma = cont = 0
outro = 'a'
while outro not in 'Nn':
    num = int(input(f'Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    outro = str(input(f'Quer continuar [S/N]? ')).strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
