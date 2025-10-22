salario = float(input('Digite o salario: '))
sal_10 = salario * (10/100) + salario
sal_15 = salario * (15/100) + salario
if salario > 1250:
    print('O valor com aumento será: {:.2f}'.format(sal_10))
else:
    print('O valor com aumento será: {:.2f}'.format(sal_15))


