m = 400
dias = c = 0

while c < m:
    c += 40
    print(f'Metros percorridos DIA: {c}')
    c -= 30
    print(f'Metros percorridos NOITE: {c}')
    dias += 1
print(f'Dias: {dias} = {c}')