#Ler o peso de 5 pessoas e informar o maior e menor
for cont in range(1, 6):
    peso = float(input(f'Digite o peso da {cont}° pessoa: '))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso encontrado é: {menor}')
print(f'E o maior peso é: {maior}')