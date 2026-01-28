"""
Docstring for al74
Closures - Funções que retornam outras funções com contexto

Possível para automatização de tarefas repetitivas
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

diga_ola = criar_saudacao("Olá")
diga_boa_tarde = criar_saudacao("Boa tarde")

print(diga_ola("Felipe"))  # Output: Olá, Felipe
print(diga_boa_tarde("Maria"))  # Output: Boa tarde, Maria

for nome in ["Ana", "Bruno", "Carla"]:
    print(diga_ola(nome))
print(diga_boa_tarde(nome))