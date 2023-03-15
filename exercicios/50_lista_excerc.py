lista = ['Maria', 'Helena', 'luiz']
lista.append('Marcos')
lista.append('Alberto')
lista.pop()
lista.append('Deise')
lista[0] = 'Marta'

i = range(len(lista))

# novo_nome = i

for indice in i:
    print(indice, lista[indice])

