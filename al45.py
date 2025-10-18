"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero) 
texto = 'Felipe'

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto:
    print(letra)