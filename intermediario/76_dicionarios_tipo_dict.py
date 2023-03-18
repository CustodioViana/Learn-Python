# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo 'par de "chave" e "valor"'.
# Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Custódio',
    'sobrenome': 'Viana',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])


print('---------------------------------------------')
# Manipulando chaves e valores em dicionários
pessoa = {} #dict

chave = 'nome'  #variável

pessoa[chave] = 'Custodio'
pessoa['sobrenome'] = 'Viana'

print(pessoa['nome'])
#ou
print(pessoa[chave])

pessoa[chave] = 'Alberto' # nesse momento estamos sobre escrevendo a varável chave com outro nome

del pessoa['sobrenome']  # deletamos o sobrenome
print(pessoa)
print(pessoa['nome'])

# if print(pessoa('sobrenome')) #usando if dessa forma quebra o sistema.
if pessoa.get('sobrenome') is None:     #se eu tentasse usar o 'if' para verificar se 'sobrenome exite ou não, 
                                        #quebraria o sistema,por isso usamos o .get na dict, sendo que se uma
                                        #variável não existe mais, ela retorna 'None', assim é possível usar o 'if'
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])


print('---------------------------------------------')
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)


print('---------------------------------------------')
# copy - retorna uma cópia rasa (shallow copy)


import copy #módulo copy, usado para fazer cópia total de um dicionário

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)


print('---------------------------------------------')
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

        # get
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))
        # pop
# nome = p1.pop('nome')
# print(nome)
# print(p1)
        # popitem
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
        # update
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# p1.update(nome='novo valor', idade=30)

# tupla = (('nome', 'novo valor'), ('idade', 30))

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)




