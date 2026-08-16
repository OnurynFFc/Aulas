# try, except, else e finally
try:
    print('Abrir arquivo')
    0/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu zero')
except IndexError:
    print('Dividiu zero')
except (NameError, ImportError):
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print(222)
