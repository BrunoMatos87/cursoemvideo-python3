from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
anos = date.today().year - ano_nascimento
ano_falta = anos - 18
ano_passou = anos - 18
if anos < 18:
    print('Você tem {} anos. Só pode se alistar com 18 anos'.format(anos))
    print('Faltam {} anos para o seu alistamento'.format(ano_falta).replace('-', ''))
elif anos == 18:
    print('Você tem {} anos. Já pode se alistar'.format(anos))
elif anos > 18:
    print('Você tem {} anos. Só pode se alistar com 18 anos'.format(anos))
    print('Ja se passaram {} anos do seu alistamento'.format(ano_passou))


