# Delimitadores de linha (Gera quebrade linha)
# \r\n -> CRLF
# \n -> LF

#sep= Utilizado para colocar um separado entre dois argumentos com "," para separalos
#end= Utilizado pra incluir argumento no fim da linha, pode se usar \n dentro normalmente

print(12, 34, 'sem formatação')
print(12, 34, 'com semparador', sep="-")
print(12, 34, "com separador", sep='-')
print(12, 34, 'com quebra de linha', end='\n')
print(12, 34, 'com quebra de linha antes de um argumento, argumento vai pra baxo',end='\n##')
print(12, 34)
