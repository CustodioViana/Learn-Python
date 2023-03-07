#Aulas 13 - f-string
#:.xf = fomula pra limitar casas decimais, onde o x é a quantidade de casas decimais
#:,.xf = em alguns caso é possível incluir a vírgulas.

nome = "Junior Viana"
altura = 1.70
peso = 74
imc = peso / ((altura * altura))  
#pode ser peso / ((altura ** 2)) também

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
