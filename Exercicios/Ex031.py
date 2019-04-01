km = float(input('Quantos km de viagem? '))
# Simplificado # total = km * 0.5 if km <= 200 else km *0.45

if km <= 200:
    total = km * 0.5
else:
    total = km * 0.45
print(f'Sua viagem de {km}KMs custará R${total:.2f}')
