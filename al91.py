#Introdução às Generator dunctions em python
# generator = (n for n in range(1000000)) -> função que sabe pausar

def generator(n=0, maximum=10):
   while True:
       yield n
       n += 1
       if n >= maximum:
            return

       
   



gen = generator(maximum=10000)
for n in gen:
    print(n)