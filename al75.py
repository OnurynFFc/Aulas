#Exercícios
#Crie funçoes que duplicam, triplicam e quadruplicam
#o número recebido como parâmetro.

def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(8))
print(quadriplicar(9))