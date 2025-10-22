def fatorial(num1 = 1, show=False):
    '''
    -> Calcula o fatorial de um numero.
    :param nuumero: numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um numero.
    '''


    f = 1
    for c in range(num1, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, False))
#help(fatorial)
