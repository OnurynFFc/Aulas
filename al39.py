'''
iterando strings com ehile
'''

#........01234567891011
nome = input('Digite seu nome: ')
tam = len(nome)
print(tam)
print(nome)

tam_nome=0
nova_string =''
while tam_nome < len(nome):
    nova_string+= f'{nome[tam_nome]+'*'}'  
    tam_nome+=1

print(nova_string)

    # if tam_nome ==12:
    #     break
# print(nova_string)
# print(f'{nome[tam_nome]+'*'}')
    # nova_string=nova_string*tam_nome
    # print(nova_string)
