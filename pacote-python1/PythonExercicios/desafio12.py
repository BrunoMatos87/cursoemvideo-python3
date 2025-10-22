preco = float(input('Qual valor do produto? ' ))
preco_desc = preco - (preco * 5 / 100)
print('O valor com desconto é {:.2f}'.format(preco_desc))