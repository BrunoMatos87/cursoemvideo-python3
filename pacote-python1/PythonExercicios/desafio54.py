from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0

for pessoa in range(1, 8):
    ano_nasc = int(input('Qual ano de nascimento {}ª pessoa: '.format(pessoa)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('A soma de maiores de 18 é {}. E a soma de menores de 18 é {}'.format(maior, menor))





