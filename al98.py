#módulos pytho são recarregados ma vez

import importlib #recarregar o módulo

import al98_m

print(al98_m.varia)

for i in range(10):
    # print(i)
    importlib.reload(al98_m)

print('FIM')