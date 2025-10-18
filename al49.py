"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [1,2,3,4]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(5)# adicionando 
lista.pop()#remove o ultimo
lista.append(6)# adicionando
ultimo_valor = lista.pop(3)#remove o ultimo
print(lista, 'Removido', ultimo_valor)
