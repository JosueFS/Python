nome = str(input('Digite seu nome completo: '))
print('1. Todas em Maiúsculas: {}'.format(nome.upper()))
print('1. Todas em Minúsculas: {}'.format(nome.lower()))
qtd = len(nome) - nome.count(' ')
print('Quantidade de letras (sem espaços): {}'.format(qtd))
div = nome.split()
print('Quantidade de letras do primeiro nome: {}'.format(len(div[0])))