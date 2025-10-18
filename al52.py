"""
Cuidados com dados mutáveis
   = -copiando o valor (imutáveis)
   = -apontapara o mesmo valor na memória (mutável)

"""
# nome = 'Felipe'
# outra=nome
# nome = 'Joao'

# print(nome)
# print(outra)

lista_a = ['luiz', 'maria']
lista_b = lista_a.copy()

lista_a[0]='xxxx'
print(lista_b)
print(lista_a)