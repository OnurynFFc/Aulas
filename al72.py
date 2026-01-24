#Exercicios com funções
#Crie uma função que multiplica todos os argumentos
#não nomeados recebidos
#Retorne o resultado da multiplicação em uma variável
#e imprima o valor da variável

def multiplica(*args):
    resultado=1
    for numenro in args:
        resultado *=numenro
    return resultado

mostrar = multiplica(1,2,3,4,5)

print(mostrar)



#Crie uma função que fala se um número é par ou ímpar
#Retorne se o número é par ou ímpar em uma variável

def parOuImpar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

num = int(input("digite um numero:"))
resultado = parOuImpar(num)
print(f"O númenro {num} é {resultado}.")