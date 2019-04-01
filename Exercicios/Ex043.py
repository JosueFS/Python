peso = float(input('Digite o peso(Kg): '))
alt = float(input('Digite o altura(m): '))

imc = peso / (alt ** 2)

print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print(f'Cuidado, você está ABAIXO do seu peso ideal!')
elif imc < 25:
    print(f'PARABÉNS, Você está no peso ideal!')
elif imc < 30:
    print(f'Você está um POUCO ACIMA do Peso.')
elif imc < 40:
    print(f'Você está no nível de OBESIDADE!')
else:
    print(f'ATENÇÃO! Você está no nível de OBESIDADE MÓRBIDA, Cuidado!!')