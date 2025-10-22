from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
categoria: int = date.today().year - ano_nascimento
if categoria <= 9:
    print('Sua idada é {}, e sua categoria é MIRIM.'.format(categoria))
elif categoria <= 14:
    print('Sua idada é {}, e sua categoria é INFANTIL.'.format(categoria))
elif categoria <= 19:
    print('Sua idada é {}, e sua categoria é JUNIOR.'.format(categoria))
elif categoria <= 25:
    print('Sua idada é {}, e sua categoria é SENIOR.'.format(categoria))
else:
    print('Sua idada é {}, e sua categoria é MASTER.'.format(categoria))