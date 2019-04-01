frase = 'Curso em Vídeo Python'
# frase = '   Aprenda Python  '
# Fatiamento
pedaço = frase[3:13]
tamanho = len(frase)
qtd = frase.count('o',0,13)

# Se retornar -1 é porque não existe a string informada no argumento
pesquisa = frase.find('deo')

# Retorna um valor boleano
teste = 'Curso' in frase

nova = frase.replace('Python', 'Android')
maiu = frase.upper()
minu = frase.lower()
cap = frase.capitalize()
tit = frase.title()

# Elimina os espaços excedentes
ajuste = frase.strip()
ajusteEsq = frase.lstrip()
ajusteDir = frase.rstrip()

# Dividir uma String, cada palavra é armazenada em uma mesma lista
div = frase.split()

# Junção
juntar = ' '.join(div)

print("""\nAs lembranças que você me deu
Valem mais que toda história de um cara como eu
Lembro de um beijo seu
Penso no acontecido
Fico agradecido
Eu quero estar com você""")

# print(juntar)
