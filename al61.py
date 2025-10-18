'''
Listas de listas e seus indices
'''
salas = [
    #0              1
    ['maria', 'helena', ],#0

    #0
    ['eliane', ],#1
    #0      1       2
    ['luiz','joao', 'eduarda', ], #2

]

# print(salas)

for sala in salas:
    print(f'A sala é {sala}')
    for item in sala:
        print(item)