num_int = int(input('Digite um numero inteiro: '))
tot = 0
for c in range (1, num_int + 1):
    if num_int % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num_int, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('Não é primo')
