#Aulas 12 - Execício Calculos - IMC

nome = "Junior Viana"
altura = 1.70
peso = 74
imc = peso / ((altura * altura))

print(nome, 'tem', float(altura), 'de altura,')
print('Pesa', peso, 'quilos e seu imc é')
#Aredondar float
print(round(imc))
#Limitar duas casas decimais em float
print('{:.2f}'.format(imc))
