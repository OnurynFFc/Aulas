#dir, hasttr e getattr em python
string ="felipe"
metodo = 'a'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe', metodo)
