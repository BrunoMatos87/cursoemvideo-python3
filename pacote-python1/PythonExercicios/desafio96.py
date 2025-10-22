def area(larg, comp):
    soma = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {soma}m2.')


print('  CONTROLE DE TERRENOS  ')
print('-'*30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
