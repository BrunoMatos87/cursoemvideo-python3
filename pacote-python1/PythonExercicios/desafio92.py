from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] == 0:
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f'  - {k} tem o valor {v}.')
else:
     pessoa['contratcao'] = int(input('Ano de Contratação: '))
     pessoa['salario'] = float(input('Salário: R$ '))
     pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratcao'] + 35) - date.today().year)
     print('-=' * 30)
     for k, v in pessoa.items():
         print(f'  - {k} tem o valor {v}.')