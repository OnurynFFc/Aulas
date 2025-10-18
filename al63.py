# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #0              1
    ['maria', 'helena', ],#0

    #0
    ['eliane', ],#1
    #0      1       2
    ['luiz','joao', 'eduarda', ], #2

]

# a,b,c,*_,ap ,u =lista
# print(ap,u)


print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')