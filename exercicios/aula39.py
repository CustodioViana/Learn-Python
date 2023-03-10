linha = (20*'-')
"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

# print('Minha resolução')
# print(linha)

# nome = input('Please, enter your name: ')
# cont_nome = len(nome)
# letra = 0

# while letra <= (cont_nome - 1):
#     print('*', nome[letra], '*')
#     letra += 1

# print(f'Seu nome tem {cont_nome} letras')

# print(linha)
# print('Resolução do professor')

# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)


print(linha)
print('Reestruturação do execercício')

nome = input('Please, enter your name: ')
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(f'{novo_nome}*')