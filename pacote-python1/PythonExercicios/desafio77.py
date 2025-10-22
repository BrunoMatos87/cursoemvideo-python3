palavra = ('aprender', 'ensinar', 'programar', 'linguagem')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

