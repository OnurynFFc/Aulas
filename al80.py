'''
Docstring for al80
Sets em Python
Conjunto (set) - coleção não ordenada de elementos únicos
Elementos imutáveis (números, strings, tuplas)
Criação de sets usando chaves {} ou a função set()
Operações comuns: união, interseção, diferença, adição e remoção de elementos

São eficientes para testes de associação (verificar se um elemento está presente)
removem duplicatas automaticamente
não suportam indexação ou fatiamento

Métodos comuns:
add() - Adiciona um elemento ao set
remove() - Remove um elemento do set (gera erro se o elemento não existir)
discard() - Remove um elemento do set (não gera erro se o elemento não existir)
clear() - Remove todos os elementos do set
union() - Retorna a união de dois sets
 cria um set vazio
# criando um set com elementos
s2 = {1, 2, 3, 4}  # Duplicatas serão removidas
print(s2)  # Saída: {1, 2, 3, 4}
'''
# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1]  # Lista com elementos duplicados
# s1 = set(l1)
# l2 = list(s1)
# print(l2)  # Saída: {1, 2, 3} - Duplicatas são removidas

s1 ={1,2,3}
# print(3  in s1)

for numero in s1:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos