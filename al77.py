#Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome' #chave dinâmica

pessoa[chave] = 'Felipe'
pessoa['sobrenome'] = 'Silva'

print(pessoa[chave])  # Acesso ao valor usando a variável chave

pessoa[chave] = 'Maria'  # Atualizando o valor da chave dinâmica
print(pessoa[chave])  # Acesso ao valor usando a variável chave

print(pessoa)

del pessoa['sobrenome']  # Removendo a chave 'sobrenome'
print(pessoa)  # Verificando o dicionário após a remoção


if pessoa.get('sobrenome') is None:
    print('Chave "sobrenome" não encontrada!')