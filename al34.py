'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdaeira~
loop infinito -> Não tem fim
'''
condicao =True

while condicao:
    nome=input('Qual seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break
print('acabou')