s = float(input('Qual é o salário do funcionário? '))
if s <= 1250:
    n = s * 1.15
else:
    n = s * 1.10
print(f'O novo salário do funcionário é R${n:.2f}')
