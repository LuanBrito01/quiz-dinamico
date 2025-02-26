perguntas = [
    {
        'Pergunta': 'Quanto é 25²?',
        'Opções': ['50', '225', '625', '550'],
        'Resposta': '625',
    },
    {
        'Pergunta': 'Quanto é a raiz quadrada de 144?',
        'Opções': ['12', '22', '16', '14'],
        'Resposta': '12',
    },
    {
        'Pergunta': 'Na matemática, qual desses números tem um significado especial?',
        'Opções': ['5', '2', '7', '1'],
        'Resposta': '7',
    },
    {
        'Pergunta': 'Qual o ponto de ebulição da água?',
        'Opções': ['45º', '100º', '60º', '85º'],
        'Resposta': '100º',
    },
    {
        'Pergunta': 'Quantos meses do ano tem 31 dias?',
        'Opções': ['7', '2', '5', '10'],
        'Resposta': '7',
    },
]

quantidade_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    quantidade_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        quantidade_acertos += 1
        print('Você acertou 🤩')
    else:
        print('Você errou 🙁')
    
    print()

if quantidade_acertos >= 3:
    print(f'Parabéns 🤩. Você conseguiu acertar {quantidade_acertos} de {len(perguntas)} perguntas.')
else:
    print(f'Você acertou apenas {quantidade_acertos} de {len(perguntas)} perguntas 😕. Tente novamente.')
