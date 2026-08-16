#raise - lançando exceções (erros)
#posso lancar meus erros no programa
def nao_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividor por zero')
    return True
    

def sem_strings(n):
    tipoN = type(n)
    if not isinstance(n,(float, int)):
            raise TypeError(
                 f'{n} deve ser int ou float'
                 f'{tipoN.__name__} enviado'

                            )
    return TypeError

def divide(n,d):

    sem_strings(n)
    sem_strings(d)
    nao_zero(d)
    return n/d
    

print(divide(8,'0'))

