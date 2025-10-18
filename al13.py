#Formatação de strings
# var: , .xf| diz quantos numeros dps da virgula vai querer
nome = "felipe"
altura= 1.77
peso = 63
# p= ... elipese
imc = peso / altura ** 2
# f-strings
linha= f'{nome} tem {altura:,.1f} de altura'
linhad = f'pesa {peso} kg'
linhat = f'seu imc é: {imc:.2f}'
print(linha)
print(linhad)
print(linhat)
#print(nome,'tem', altura, 'de altura')
#print('pesa:', peso)
#print('seu imc é:', imc)