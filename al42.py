frase = 'felipe'

# print(frase.count(''))
i = 0 
qtd_apareceu_mais_vezes = 0
letra_m = ''

while i < len(frase):
    letra_atual = frase[i]
    qt_letra = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qt_letra:
        qtd_apareceu_mais_vezes = qt_letra
        letra_m = letra_atual
    
    i+=1 

print(f'A letra que apareceu mais vezes foi "{letra_m}".'
f'Apareceu {qtd_apareceu_mais_vezes}')