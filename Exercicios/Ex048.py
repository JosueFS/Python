soma = 0
qtd = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        qtd += 1
print(f'A soma de todos os {qtd} numeros é igual a {soma}')