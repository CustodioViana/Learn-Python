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


nome = input('Please, enter your name: ')
cont_nome = len(nome)
letra = 0

while letra <= (cont_nome - 1):
    print(nome[letra])
    letra += 1

print(f'Seu nome tem {cont_nome} letras')