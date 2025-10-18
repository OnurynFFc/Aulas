# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entada = input('[E]ntrar [S]air')
senha = input('Senha: ')

senha_p = '123456'
if entada=='E' and senha == senha_p:
    print('Entrar')
else:
    print('Sair')

print( True and False and True)
print(True and 0 and True)