"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
# """
# try:
#     numero = input('digite um numero inteiro: ')
#     numeroint= int(numero)
#     resto = numeroint%2

    
#     if resto==0:
#         print(f'o numero {numero} é par')
#     else:
#         print(f'o numero {numero} é impar')
# except:
#     print('Não é um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# try:
#     hora= int(input("Me informe o horário: "))

#     if hora <= 11:
#         print('BOM DIA!')
#     elif hora >=12 and hora<=17:
#         print('BOA TARDE!')
#     elif hora>=18 and hora<=23:
#         print('BOA NOITE!')
#     else:
#         print('Horário incorreto')
# except:
#     print('digite apenas numeros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tam= len(nome)

if tam>1:
    if tam<=4:
        print('Seu nome é curto')
    elif tam>=5 and tam<=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite mais de uma letra')