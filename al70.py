"""
Docstring for al70
Retorno de valores das funçoes com return
"""

def soma(a, b):
    if a + b > 10:
        return 10,20
    return a + b




# variavel = soma(2, 3)
# variavel = int('1')
# print(variavel)

soma1 = soma(2, 3)
soma2 = soma(5, 7)
print(soma(11,2))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'