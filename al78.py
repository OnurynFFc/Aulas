"""
Docstring for al78

Métodos de dicionários em Python
len() - Retorna o número de itens no dicionário
clear() - Remove todos os itens do dicionário
copy() - Retorna uma cópia rasa do dicionário (shallow copy) 
values() - Retorna uma visão dos valores no dicionário
items() - Retorna uma visão dos pares chave-valor no dicionário
keys() - Retorna uma visão das chaves no dicionário
get() - Retorna o valor para a chave especificada, ou None se a chave não existir
pop() - Remove a chave especificada e retorna o valor correspondente
popitem() - Remove e retorna um par chave-valor arbitrário do dicionário
update() - Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor
setdefault() - Retorna o valor da chave especificada. Se a chave não existir
"""

p1 ={
    'nome': 'Luiz',
    'sobrenome': 'Otávio',
}


p1.update({'nome': 'João', 'idade': 30})  # Atualiza o dicionário com novos pares chave-valor
print(p1)



# sobrenome = p1.popitem()  # Remove e retorna um par chave-valor arbitrário
# print(sobrenome)  # ('sobrenome', 'Otávio')
# print(p1)
# # nome = p1.pop('nome')  # Remove a chave 'nome' e retorna o valor associado
# print(nome)  # Luiz

# print(p1.get('nome', 'Chave não encontrada'))  # Luiz


# import copy

# d1 = {
#     'c1':1,
#     'c2':2,
#     'l1':[10,20,30],
# }
# d2 = copy.deepcopy(d1)  # Cópia profunda

# d2['c1'] = 1000
# d2['l1'][0] = 9999


# print(d1)
# print(d2)

# pessoa = {
#     'nome': 'Ana',
#     'idade': 30,
#     'cidade': 'São Paulo'
# }

# pessoa.setdefault('sobrenome', 'souza')
# print(pessoa['sobrenome'])


# print(len(pessoa))  # Retorna o número de itens no dicionário
# print(list(pessoa.keys()))
# print(list(pessoa.values()))    # Retorna uma visão dos valores no dicionário
# print(list(pessoa.items()))    # Retorna uma visão dos pares chave-valor no dicionário

# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')  # Iteração sobre chaves e valores

