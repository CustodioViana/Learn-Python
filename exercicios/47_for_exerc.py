"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""



palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0






# Primeira Tentativa

# palavra_secreta = input('Digite uma palavra: ')
# letras_achadas = []
# tentativas = 0

# for i in palavra_secreta:
#     letras_achadas.append('*')

# while True:
#     letras = input('Digite uma letra: ')
#     if len(letras) > 1:
#         print('Digite somente uma letra')
#     elif len(letras) == 0:
#         print('Digite pelo menos uma letra')
#         continue
    
#     tentativas += 1

#     if letras in palavra_secreta:
#         letras_achadas += letras

#     for i in range(len(palavra_secreta)):
#         if i in letras_achadas:
#             print(i)
#         else:
#             print('*')


    

# Código do ChatGPT para fins de estudos

# palavra_secreta = input("Digite a palavra secreta: ")
# letras_descobertas = ["*" for letra in palavra_secreta]
# tentativas = 0
# acertou = False

# for letra in letras_descobertas:
#     if "*" not in letras_descobertas:
#         break
        
#     letra = input("Digite uma letra: ")
#     tentativas += 1
#     acertou = False
    
#     for i in range(len(palavra_secreta)):
#         if letra == palavra_secreta[i]:
#             letras_descobertas[i] = letra
#             acertou = True
    
#     palavra_atual = ""
#     for letra_atual in letras_descobertas:
#         palavra_atual += letra_atual
    
#     print(palavra_atual)
    
#     if not acertou:
#         print("Errou!")
    
#     print("Tentativas:", tentativas)
    
# print("Parabéns, você descobriu a palavra secreta em", tentativas, "tentativas!")