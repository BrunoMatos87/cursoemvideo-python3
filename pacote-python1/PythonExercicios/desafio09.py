num = int(input('Digite o numero para tabuada: '))

for i in range(1,11):
    resultado = num * i
    print('{} x {:2} = {}'.format(num, i, resultado))
