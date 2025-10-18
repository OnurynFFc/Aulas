"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z): #definição
    print(f'{x=} {y=}, {z}',"|","x + y + z = ",{x+y+z})


soma#nome da função
soma(2,0,3)#chamamento de função
soma(y=2, x=1, z=3)

print(1,2,3, sep='-')