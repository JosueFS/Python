n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'O aluno tirou {n1:.1f} e {n2:.1f}, a média é {media:.1f}.')

if media < 5:
    print(f'O aluno está REPROVADO.')
elif media < 6.9:
    print(f'O aluno está de RECUPERAÇÃO.')
else:
    print(f'O aluno está APROVADO!')
