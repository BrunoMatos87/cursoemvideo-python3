print('{:=^40}'.format('  LOJAS MATOS   '))
preco_norm = float(input('Preços das compras: R$ '))

print('''FORMAS DE PAGAMENTOS:
    [ 1 ] à vista dinheiro / cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no Cartão
    [ 4 ] 3x ou mais
    ''')
forma_pag = int(input('Qual a forma de pagamento: '))
if forma_pag == 1:
    preco_desc = preco_norm - (preco_norm * 10 / 100)
    print('O preço a pagar com 10% de desconto é R${}'.format(preco_desc))
elif forma_pag == 2:
    preco_desc = preco_norm - (preco_norm * 5 / 100)
    print('O preço a pagar com 5% de desconto é R${}'.format(preco_desc))
elif forma_pag == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(preco_norm / 2))
    print('O preço a pagar é R${}'.format(preco_norm))
elif forma_pag == 4:
    preco_juros = preco_norm + (preco_norm * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    valor_parcelas = preco_juros / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas, valor_parcelas))
    print('O preço total a pagar é R${}'.format(preco_juros))
else:
    print('Digitou opção errada. Tente novamente.')