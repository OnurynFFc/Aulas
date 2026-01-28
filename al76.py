"""
Docstring for al76
dicionários - Estrutura de dados chave-valor
tipo dict
chaves únicas e imutáveis
valores podem ser mutáveis ou imutáveis

chaves podem ser consideradas índices
acesso rápido aos valores

o VALOR de uma chave pode ser qualquer tipo de dado como:
- números
- strings
- listas
- tuplas
- dicionários

usamisos chaves para armazenar e acessar os valores

Imutaveis: strings, números, tuplas
Mutáveis: listas, dicionários, conjuntos
"""
pessoa = {
    'nome': 'Ana',
    'idade': 25,
    'cidade': 'São Paulo',
    'altura': 1.65,
    'hobbies': ['leitura', 'viagem', 'fotografia'],
    'enderco': {
        'rua': 'Rua das Flores',
        'numero': 123,
        'bairro': 'Jardim das Acácias'}
    }


print(pessoa['nome'], pessoa['idade'])  # Acesso ao valor pela chave

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')  # Iteração sobre chaves e valores