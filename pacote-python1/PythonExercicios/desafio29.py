velocidade = float(input('Qual velocidadedo carro? '))
if velocidade > 80:
    print('Você foi multado')
    print('A multa vai custar: {}'.format((velocidade - 80) * 7))