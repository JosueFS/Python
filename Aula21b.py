from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    if idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input(f'Digite o ano de nascimento: '))
print(voto(nasc))