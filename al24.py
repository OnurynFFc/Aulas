# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
#nome = 'Felipe'
#print(nome[2])
#print(nome[-4])
#print('l' in nome)
#print('el' in nome)
#print(10* '=')
#print('el'not in nome)

nome = input('digite seu nome: ')
encontrar = input('Digite oq deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

