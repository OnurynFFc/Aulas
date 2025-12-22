'''
Escopo de funções em Python
Escopo de variáveis: local, não local, global e embutido
Escopo significa a região do código onde uma variável é reconhecida
O escopo global é o escopo onde a variável é reconhecida em todo o código
o escopo local é o escopo onde a variável é reconhecida apenas dentro de uma função
o escopo não local é o escopo onde a variável é reconhecida em funções aninhadas
o escopo embutido é o escopo onde a variável é reconhecida em todo o o código, mas é definida pelo Python
'''

x = 10 # variável global

def escopo():
    x = 1

    def escopo_interno():
        y=2      
        print(x,y)
    escopo_interno()
    print(x)

print(x)
escopo()
print(x)