#Empacotamento e desempacotamento de dicionarios

# a,b = 1, 2
# a,b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoas.items()
# print(a1, a2, b1, b2)

# for chave, valor in pessoas.items():
#     print(chave, valor)



pessoas = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

dados_pessoa ={
    'idade': 30,
    'altura': 1.80,
}

pessoas_completa = {**pessoas, **dados_pessoa}
# print(pessoas_completa)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

# mostrar_argumentos_nomeados(nome='Luiz', sobrenome='Miranda', idade=30, altura=1.80)
# mostrar_argumentos_nomeados(**pessoas_completa)

configaracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostrar_argumentos_nomeados(**configaracoes)