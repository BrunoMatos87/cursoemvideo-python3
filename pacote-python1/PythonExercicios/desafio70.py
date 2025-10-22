total_compra = prod_maior = menor_preco = cont = 0
nome_prod_barato = ''

while True:
    print('-' * 25)
    print('LOJA SUPER BARATÃO')
    print('-' * 25)
    nome_prod = str(input('Nome do Produto: ')).strip()
    preco_prod = float(input('Preço: R$ '))
    cont += 1
    total_compra += preco_prod
    if preco_prod > 1000:
        prod_maior += 1
    if cont == 1 or preco_prod < menor_preco:
        menor_preco = preco_prod
        nome_prod_barato = nome_prod
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total_compra:.2f}')
print(f'Temos {prod_maior} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nome_prod_barato} que custa R${menor_preco:.2f}')
