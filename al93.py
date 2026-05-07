#Try, Except, else e finally

# c = a/b

# a = 18
# b = 0
# print(b[0])
# print('l1')
# c = a/b
# print('l2')

try: #silenciar erro
    a = 18
    b = 0
    # print(b)
    # print('l1')
    c = a/b
    # print('l2')


except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('nome não definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print("MGS", error)
    print("Nome:", error.__class__.__name__)

except Exception:
    print('Erro desconhecido')

print('continuar')