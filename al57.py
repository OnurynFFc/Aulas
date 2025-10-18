"""
Enumerate - enumera iteráveis  (indices)
"""
lista = ['felipe','Gabriel', 'gustavo']
lista.append('diego')

# lista_enumerada=list(enumerate(lista))
# print(lista_enumerada)

for nome in enumerate(lista):
    indice,nomes = nome
    print(indice, nomes)

# for tuplas in enumerate(lista):
#     for valor in tuplas:
#         print(f' \t{valor}')
