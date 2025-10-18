'''

Intodução ao  try / except

try -> tenta execurat o código

except -> ocorreu algum erro ao tentar xecutar
'''
numero_str = input('Vou dobra o numeo: ')

try:
    numero_float = float(numero_str)
    print(f'o dobo de {numero_str} é {numero_float * 2:.0f}')
    
except:
    print('Isso não é um numero')

''' 
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'o dobo de {numero_str} é {numero_float * 2:.0f}')
else:
    print('Isso não é um numero')
'''