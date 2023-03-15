"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)