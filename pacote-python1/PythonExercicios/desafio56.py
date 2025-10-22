idade = 0
idade_soma = 0
sexo = ''
idade_homem_velho = 0
nome_homem_velho = ''
soma_mulheres = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()[0]

    idade_soma += idade
    media = idade_soma / 4 ## achar a media
    if sexo == 'M' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
        soma_mulheres = soma_mulheres + 1 ##quantidade de mulheres < 20

print('A media de idade é {:.2f}'.format(media))
print('O homem mais velho é {}'.format(nome_homem_velho))
print('Soma de mulheres com menos de 20 anos é {}'.format(soma_mulheres))


