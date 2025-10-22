valor_casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual salario atual? '))
anos = int(input('Em quantos anos vai pagar? '))
prestacao = valor_casa / (anos * 12)
if prestacao <= salario * 0.3:
    print('Parabens, foi aprovado, a prestção ficou no valor de R$ {:.2f}'.format(prestacao))
else:
    print('Infelizmente o emprestimo foi negado')