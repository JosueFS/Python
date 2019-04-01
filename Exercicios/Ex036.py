vCasa = float(input('Digite o valor da Casa R$:'))
salario = float(input('Digite o valor do salario R$:'))
anos = int(input('Digite em quantos anos deseja pagar: '))

limite = salario * 0.3
parcela = vCasa / (anos * 12)

print(f'Para pagar a casa no valor de R${vCasa:.2f} em {anos} anos', end='')
print(f' será parcelado em {anos*12} Parcelas de R${parcela:.2f}.')

if limite >= parcela:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
