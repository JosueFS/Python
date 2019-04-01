turma = []
aluno = []
notas = []
while (True):
    # Inserindo dados
    aluno.append(str(input(f'Nome: ')))
    notas.append(float(input(f'Nota 1: ')))
    notas.append(float(input(f'Nota 2: ')))

    # Montando estrutura da lista
    aluno.append(notas[:])
    # media
    aluno.append((notas[0] + notas[1]) / 2)
    turma.append(aluno[:])

    # Limpando as listas
    aluno.clear()
    notas.clear()

    # Condição de parada
    opt = str(input(f'Quer continuar [S/N]?'))
    if opt in 'Nn':
        break
print('=' * 50)

# Exibindo os boletins
print(f'{"N°.": <5}{"NOME": <10}{"MÉDIA": ^5}')
print('-' * 25)
for i, a in enumerate(turma):
    print(f'{(i + 1): <5}{a[0]: <10}{a[2]: ^5.2f}')
print('-' * 25)

# Mostrar notas individuais
while (True):
    opt = int(input(f'Digite o N° para ver as notas (Ou 999 Para Encerrar):'))
    if opt == 999:
        print(f'FINALIZANDO...')
        break
    print(f'Notas de {turma[opt-1][0]} são {turma[opt-1][1]}')
    print('-' * 25)

print(f'\nVOLTE SEMPRE !!')
