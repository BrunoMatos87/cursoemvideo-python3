distancia = float(input('Qual distancia da sua viagem? '))
if distancia <= 200:
    print('O valor da sua passagem vai ser {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da sua passagem vai ser {:.2f}'.format(distancia * 0.45))