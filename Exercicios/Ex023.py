n = str(input('Digite um numero (0 - 9999: ')).zfill(4)
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n[3:4], n[2:3], n[1:2], n[0:1]))

a = int(input('Digite um numero: '))

k = a // 1000 % 10
ct = a // 100 % 10
dz = a // 10 % 10
un = a // 1 % 10

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(un, dz, ct, k))