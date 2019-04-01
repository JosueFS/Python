aluno = {}
aluno['nome'] = str(input(f'Digite o nome: '))
aluno['media'] = float(input(f'Digite a média: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')