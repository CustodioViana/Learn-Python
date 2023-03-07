print('Execicio de Fatiamento')
print('-----------------------------')

"""
Peça o nome do usuário
Peça a idade do usuário
 Exiba
  Seu nome é {nome}
  Seu nome é {nome invertido}
  Seu nome tem {n} letras
  A primeira letra do seu nome é {p letra}
  A última letra do seu nome é {u letra}
Se nada for digitado em nome ou idade:
 Exiba
  "Desculpe, você deixou um ou mais campos vazios"
"""

nome = input(f'Qual é o seu nome? ')
idade = input(f'Qual é a sua idade? ')

if nome and idade != '':
    print('Seu nome é ', nome)
    print('Seu nome invertido é ', nome[::-1])
    print('Seu nome tem ', len(nome), 'letras')
    print('A primeira letra do seu nome é ', nome[0])
    print('A última letra do seu nome é: ', nome[-1:])
else:
    print('Desculpe, você deixou um ou mais campos vazios')