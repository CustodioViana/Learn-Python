"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""


# Primeira Tentativa

p_secreta = input('Digite uma palavra: ')
l_achadas = []
tentativa = 0


for i in range(len(p_secreta)):
    l_achadas.append('*')

acertou = False

while acertou == False:
    tentativa += 1
    
    letra = input('Digite uma letra: ')
    for i in range(len(p_secreta)):
        if letra == p_secreta[i]:
            l_achadas[i] = letra
            print(l_achadas)


acertou = True

for j in range(len(l_achadas)):
    if l_achadas == '*':
        acertou = False






    

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