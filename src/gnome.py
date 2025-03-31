import random as rd

n = 5
lista1 = []

# Crescente
for i in range(n):
    lista1.append(i)
    
# Decrescente
lista2 = []
for i in range(n, 0, -1):
    lista2.append(i)
    
# Aleatório
lista3 = []
for i in range(n):
    lista3.append(rd.randint(1, 101))
    
print(lista1)
print(lista2)
print(lista3)

def troca(lista, i):
    lista[i], lista[i - 1] = lista[i - 1], lista[i]
    
def gnomesort(lista):
    i = 0
    while i < len(lista):
        if i == 0 or lista[i] >= lista[i - 1]:
            i += 1
        else:
            troca(lista, i)
            i -= 1
    
    return lista
            
lista3 = gnomesort(lista3)
print(lista3)