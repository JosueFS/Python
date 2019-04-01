from random import randint
num = -1
tentativas = 0
sorteado = randint(0,10)
print(f'Sou seu computador...')
print(f'Acabei de pensar em um número entre 0 e 10.')
print(f'Será que você consegue adivinhar qual foi?')
while num != sorteado:
    num = int(input(f'Qual é seu palpite? '))
    if num < sorteado:
        print(f'Mais... Tente mais uma vez.')
    elif num > sorteado:
        print(f'Menos... Tente mais uma vez.')
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
