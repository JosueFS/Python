m = 400
d = c = 0
while c < m:
    c += 40
    print(f'DIA: {c}')
    if c >= 400:
        break
    c -= 30
    print(f'NOITE: {c}')
    d += 1
print(f'DIAS: {d} = {c}')