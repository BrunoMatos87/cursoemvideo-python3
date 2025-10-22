num = int(input('Digite o numero para tabuada: '))
for i in range(1,11):
    print('{} x {:2} = {}'.format(num, i, num*i))