import random
from time import sleep

print('\33[1;32m-=--=-'*10)
print('\33[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\33[1;32m-=--=-'*10)
num = int(input('\33[mEm que número pensei? '))
num2 = random.randint(0, 5)

print('\33[1;35mPROCESSANDO...')
sleep(2)
if num2 == num:
    print('\33[1;36mPARABÉNS, Você adivinhou que pensei no número {}!'.format(num2))
else:
    print('\33[1;31mGANHEI! Eu pensei no número {} e não no {}!'.format(num2, num))
print('\33[1;32m-=--=-'*10)