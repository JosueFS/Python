from datetime import date
pessoa = {}
pessoa['Nome'] = str(input(f'Nome: '))
nasc = int(input(f'Ano de Nascimento: '))
pessoa['Idade'] = date.today().year - nasc
pessoa['Ctps'] = int(input(f'Carteira de trabalho (0 - Não Possui): '))
if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input(f'Ano de contratação: '))
    pessoa['Salário'] = float(input(f'Salário: R$'))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - nasc
print('='*40)
for k, v in pessoa.items():
    print(f'{k}: {v}')
