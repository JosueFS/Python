num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções de conversão: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')

opcao = int(input('A opção escolhida foi: '))

if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:].upper()}')
else:
    print('Opção Inválida!')
