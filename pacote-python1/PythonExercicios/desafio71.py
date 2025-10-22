saque_50 = saque_20 = saque_10 = saque_1 = 0
resto = 0
print('='*30)
print('{:^30}'.format('BANCO BLM'))
print('='*30)
saque = int(input('Qual valor do Saque: R$ '))
resto = saque
while resto > 0:
    if saque >= 50:
        saque_50 = saque // 50
        resto = saque % 50
        print(f'Total de {saque_50} cédulas de r$50')
    if resto >= 20:
        saque_20 = resto // 20
        resto = saque % 20
        print(f'Total de {saque_20} cédulas de r$20')
    if resto >= 10:
        saque_10 = resto // 10
        resto = saque % 10
        print(f'Total de {saque_10} cédulas de r$10')
    if resto >= 1:
        saque_1 = resto // 1
        resto = saque % 1
        print(f'Total de {saque_1} cédulas de r$1')
    print('='*30)
    print('Volte sempre ao BANCO BLM! Tenha um bom dia!')
    break