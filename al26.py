"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
avr='asd'
print(f'{avr}')
print(f'{avr: >10}')
print(f'{avr: <10}.')
print(f'{avr:$^10}.')
print(f'{11000.0878777078:0=+10,.1f}')
print(f'O hexadecima de 1500 é{1500:08X}' )
print(f'{avr!r}')