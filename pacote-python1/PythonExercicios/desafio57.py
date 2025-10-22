sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Ddos inválidos. POr favor digite nomanete seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


