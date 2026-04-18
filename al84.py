#List comprehension em python
#List comprehension é uma forma rápida para criar listas a partir de iteravies

# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2 for numero in range(10)
    ]
print(lista)