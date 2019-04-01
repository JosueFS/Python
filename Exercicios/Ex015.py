km = float(input('Informe a quantidade de KMs percorridos: '))
dias = float(input('Informe a quantidade de dias de aluguel: '))
precoKm = 0.15 * km
precoDia = 60 * dias
valor = precoKm + precoDia
print('\nValor por KM: {}\nValor por dias: {}\nTotal a pagar: R${:.2f}'.format(precoKm, precoDia, valor))
