def notas (*resp, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos.
    :param resp: uma ou mais notas dos alunos (aceita varias notas)
    :param sit: valor opcional, indicando se dece ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = dict()
    r['total'] = len(resp)
    r['maior'] = max(resp)
    r['menor'] = min(resp)
    r['media'] = sum(resp)/len(resp)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas( 10, 8, 6, 8)
print(resp)
help(notas)