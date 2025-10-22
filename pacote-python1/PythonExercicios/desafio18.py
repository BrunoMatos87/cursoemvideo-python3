import math

angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(' O valor do seno é {:.2f}, cosseno é {:.2f}, tangente é {:.2f}'.format(seno, cosseno, tangente) )