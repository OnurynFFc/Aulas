# utilizando o
# break : para
# continue : pula 

contaor = 0

while contaor < 100:
    contaor+=1

    if contaor == 6:
        print('NÃO MOSTRAR')
        continue

    if contaor>=10 and contaor <=27:
        print('NÃO MOSRTE')
        continue

    print(contaor)

    if contaor == 40:
        break
    # print('edita')

print('acabou')