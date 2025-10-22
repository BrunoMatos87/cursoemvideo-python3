total_maior = total_homem = total_mulher = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [F/M] ')).strip().upper()[0]
    if int(idade) >= 18:
        total_maior += 1
    if sexo == 'M':
        total_homem += 1
    if sexo == 'F' and int(idade) < 20:
        total_mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 6 + ' FIM DE PROGRAMA ' + '=' * 6)
print(f'Total de pessoas com mais de 18 anos: {total_maior}.')
print(f'Ao todo temos {total_homem} homens cadastrado')
print(f'E temos {total_mulher} mulheres com menos de 20 anos')