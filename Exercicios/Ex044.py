print(f'{" [ FORMAS DE PAGAMENTO ] ":=^35}')
price = float(input('Total a pagar: R$'))
print('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opt = int(input('Selecione a opção desejada: '))

print(f'{"":=^30}')

if opt == 1:
    total = price * 0.9
    print('Forma de pagamento: à vista dinheiro/cheque')
elif opt == 2:
    total = price * 0.95
    print('Forma de pagamento: à vista no cartão')
elif opt == 3:
    total = price
    parcela = total/2
    print(f'Forma de pagamento: 2x de {parcela:.2f} SEM JUROS')
elif opt == 4:
    total = price * 1.2
    nParcela = int(input('Digite o número de parcelas:'))
    parcela = total / nParcela
    print(f'Forma de pagamento: {nParcela}x de {parcela:.2f} COM JUROS')
else:
    total = price
    print('Opção inválida!')

print(f'''{"":=^30}
Valor da compra: R${price}
Total a pagar: R${total}''')
