print(f'='*30)
print('{:^30}'.format('[ BANCO RICH ]'))
print(f'='*30)
total = valor = int(input(f'Quanto deseja sacar? R$'))
cedula = 50
totCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totCedula += 1
    else:
        print(f'Total de {totCedula} cédula(s) de R${cedula},00')
        if total >= 20:
            cedula = 20
        elif total >= 10:
            cedula = 10
        else:
            cedula = 1
        totCedula = 0
        if total == 0:
            break
print(f'='*30)
print(f'Volte sempre ao BANCO RICH! Tenha um bom dia!')
