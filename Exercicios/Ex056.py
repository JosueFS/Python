#Ler informações (nome, idade e sexo) de 4 pessoas e exibir:
#A Media de idade
#O homem mais velho
#Quantas mulheres tem menos de 20 anos
medIdade = 0
homem = 0
girls = 0

for c in range(1,5):
    #Entrada de dados
    print(f'{" {}° PESSOA ":-^22}'.format(c))
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip()

    #Acumulando a média
    medIdade += idade

    #Identificando o homem mais velho
    if sexo == 'M':
        homem += 1
        if homem == 1:
            oldMan = idade
            oldManName = nome
        if idade > oldMan:
            oldMan = idade
            oldManName = nome

    #Analisando quantas mulheres tem menos de 20 anos
    if idade < 20:
        girls += 1
#Media
medIdade = medIdade / 4

#Resultado
print(f'A média de idade do grupo é de {medIdade} anos.')
print(f'O homem mais velho tem {oldMan} e se chama {oldManName}.')
print(f'Ao todo temos {girls} mulher(es) com menos de 20 anos.')