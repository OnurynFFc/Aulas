"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = 'cachorro'
letras_corretas=''
tentativas = 0

while True:
    # os.system('cls')
    letra_diditada = input("Digite uma letra: ")

    if len(letra_diditada)>1:
        print("Digite apenas uma letra")
        continue

    print('bora')

    if letra_diditada in palavra:
        letras_corretas += letra_diditada

    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letras_corretas:
            # print(letra_secreta)
            # tentativas+=1
            palavra_formada += letra_secreta

        else:
            palavra_formada+= '*'
            # print("*")
    tentativas+=1
    print(f'Palavra formada {palavra_formada}')

    if palavra_formada == palavra:
        os.system('cls')
        print('Você acertou')
        print(f"A palvra era: {palavra}")
        print(f'Você tentou {tentativas} vezez')
        break
    

    # print(letras_corretas)