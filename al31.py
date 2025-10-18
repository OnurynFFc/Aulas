#id = Identidade
'''
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
v1 = "z"
v2 = "b"
print(id(v1))
print(id(v2))
'''
condicao = False
passo_if = None

if condicao :
    passo_if = True
    print('faça faça')
else:
    print('não faça algo')


if passo_if is None:
    print('Não passou no if')
else:
    print('passou no if')

