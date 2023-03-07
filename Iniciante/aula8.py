# Aula 8

nome = input("Escreva seu nome:")
sobrenome = input("Escreva seu sobrenome:")
idade = input("Escreva sua idade:")
ano = input("Escreva o ano do seu nascimento:")
m_idade = idade >= str(18)
altura = input("Qual sua altura?")


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', int(idade))
print('Ano de Nacimento:', int(ano))
print('É maior de idade?', m_idade)
print('Você mede:', float(altura))