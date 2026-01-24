'''
Docstring for al71

args -argumentos não nomeados
* - *args (empacotamento e desempacotamento de tuplas)

'''

#lembrete de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    # print(args)
    total = 0
    for numero in args:
        total += numero
        print(total)
    return total

soma_soma = soma(1, 2, 3,2,3,3,4,5,6,6)

numeros = 1,2,3,4,5,6,7,8,9,0

# print(soma_soma)

outra_soma = soma(*numeros)
print(outra_soma)

print(*numeros)

print(sum((numeros)))