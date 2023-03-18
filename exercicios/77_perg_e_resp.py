# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def calculo(operacao):
    def numero(num):
        return num == operacao
    return numero


def true_false(resposta):
    if resposta is True:
        return f'Você acertou a resposta.'
    return f'Você errou a resposta'


indice = 0
cont_false = 0
cont_true = 0

while True:
    if indice >= len(perguntas):
        break   
    try:

        print(perguntas[indice]['Pergunta'])
        digitada_1 = input(f"Digite um númerp entre as opções {perguntas[indice]['Opções']}\n"
                           ": ")
        resposta_1 = perguntas[indice]['Resposta']
        escolha_1 = calculo(resposta_1)
        resp = true_false(escolha_1(digitada_1))
        print(resp)

        if resp == True:
            cont_true += 1
        else:
            cont_false += 1

        if indice < len(perguntas):
            indice += 1
        print()
    except:
        ('Digite um número.')
print()
print(f'Você acertou {cont_true}\n'
      f'Você acertou {cont_false}'
      )


print('-----------------------------------------')
print('Resposta do Professor')


# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
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
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')