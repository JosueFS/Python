from math import cos, sin, tan, radians
n = float(input('Digite o angulo a ser calculado: '))
c = cos(radians(n))
s = sin(radians(n))
t = tan(radians(n))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s, c, t))
