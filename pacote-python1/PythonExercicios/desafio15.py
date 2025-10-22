dias = float(input('Digite a quantidade de dias : '))
km_rod = float(input('Digite a quantidade de km percorrido: '))
preco = (km_rod * 0.15) + (dias * 60)
print('O valor a pagar é {:.2f}'.format(preco))