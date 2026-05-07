#Generator expression, Iterables e Iterator em python
import sys
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for n in generator:
    print(n)