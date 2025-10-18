#Calculadora em python

while True:

    n1 = input('Digite um número: ')
    n2 = input('Digite um número: ')
    op = input('Digite um operador: [+] [-] [*] [/] ')
    rest = 0
 
 ############Validações
    numeros_vallidos = None

    try:
        n1_float= float(n1)
        n2_float= float(n2)
        numeros_vallidos = True
    except:
        numeros_vallidos = None

    if numeros_vallidos is None:
        print('Um ou ambos dos numeros são inválidos')
        continue

    op_permitidos='+-/*'

    if op not in op_permitidos:
        print('Operação inválida')
        continue

#Operações
    if op == '+':
        rest = n1_float + n2_float
    elif op == '-':
        rest = n1_float - n2_float
    elif op == '*':
        rest = n1_float* n2_float
    elif op == '/':
        rest = n1_float / n2_float
    # else:
    #     print('Operação impossível')
    
    print(rest)

    ##### Verificando 
    sair = input('Quer sair? [s]Sim [n]Não : ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break
    

