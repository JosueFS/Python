vel = int(input('Informe a velocidade do veiculo: '))
multa = (vel - 80) * 7
if multa > 0:
    print('\33[31mVocê foi multado por exceder o limite de 80KM/h em \33[1;33mR${:.2f}'.format(float(multa)))
print('\33[1;32mTenha um bom dia, Dirija em segurança!')
