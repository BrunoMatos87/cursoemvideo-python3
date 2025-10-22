num1 = int(input('Digite um numero: '))
mult = num1
fatorial = 1
print('Calculando {}! = '.format(num1), end='')
while num1 > 0:
    print('{}'.format(num1), end='')
    print(' x ' if num1 > 1 else ' = ', end='')
    fatorial *= num1
    num1 = num1-1
print('{}'.format(fatorial))

