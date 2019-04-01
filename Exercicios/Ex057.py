sexo = str(input(f'Informe seu sexo [M/F]: ')).strip()

while sexo not in 'MmFf':
    sexo = str(input(f'Dados inválidos. Por favor, informe seu sexo: ')).strip()
print(f'Sexo {sexo.upper()} registrado com sucesso.')