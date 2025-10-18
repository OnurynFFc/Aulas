"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Qual seu nome?: ')
idade = input('Qual sua idade?: ')

if nome=='' and idade=='':
    print('Desculpa, você deixou os campos vazios =(')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ivertido é {nome[::-1]}')
    if ' ' in nome:
        print('tem espaços')
    else:
        print('não tem espaços')
    print(f'Seu nome tem: {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')



