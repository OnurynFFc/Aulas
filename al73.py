"""
Docstring for al73
Higher order functions - Funções que retornam outras funções
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)



print(executa(saudacao, "Bom dia!", "João"))