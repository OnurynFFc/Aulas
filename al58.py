'''
Exercício:
Progama de lista de super mercado
Oq usuário pode fazer:
    Inserir os itens na sua lista
    Apagar itens da lista
    Listar os itens
Oq não pode:
    Não pode listar se a lista estiver vazia
    Apagar índices vazios

'''

lista_de_compra=[]
while True:
    
    print('Selecione qual ação deseja')
    operacao=input('[i]Inserir  [a]Apagar    [l]Listar  [s]Sair:')

    if operacao == 'i':
        item = input('O quee deseeja adicioar à lista?: \n')
        lista_de_compra.append(item)
        continue
    elif operacao == 'l':
        try:
         for compras in enumerate(lista_de_compra):
            a,b = compras
            print(a,b)
            continue
        except:
            print('Não é possível apagar uma lista uma lista vazia')
            continue
    elif operacao == 'a':
       try:
            print('Qual indice deseja apagar: ')
            indice=int(input())
            lista_de_compra.pop(indice)
            continue
       except:
            print('Não é possível apagar um indice de uma lista vazia')
            continue
    elif operacao=='s':
        break
    else:
        print('operação indiponivel')
        ...
    