def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato == False else moeda(res)


def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato == False else moeda(res)

def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa / 100)
    return res if formato == False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato == False else moeda(res)

def moeda(preco = 0, moeda='R$', formato = False):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco = 0, txaum = 10, txred = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{txaum}% de aumento: \t{aumentar(preco, txaum, True)}')
    print(f'{txred}% de redução: \t\t{diminuir(preco, txred, True)}')
    print('-' * 30)
    return
