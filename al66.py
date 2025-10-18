'''
Introdução às funções (def) em puthon
Funções são trechos de códigos usados para replicar
determida açã do ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
'''

# def imprimir(a, b, c):#Parâmetro é a variável
#     print('Salve1')
#     print('Salve2')
#     print('Salve3')


# imprimir(1,2,3)#Argumento é o valor da variável
def imprimir(a, b, c):#Parâmetro é a variável
    print(a,b,c)


imprimir(1,2,3)#Argumento é o valor da variável
imprimir(4,5,6)

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}')
saudacao('felipe')
saudacao()