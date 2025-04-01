import random as rd

n = 5

lista1 = []

#Crescente
for i in range(n):
    lista1.append(i)

#Decrescente
lista2 = []
for i in range(n, 0, -1):
    lista2.append(i)

#Aleatório
lista3 = []
for i in range(n):
    lista3.append(rd.randint(1,101))


print(lista1)
print(lista2)
print(lista3)

def shell_sort(lista):

    distancia = len(lista) // 2
    while distancia > 0:
        i = distancia
        while i < len(lista):
            temp = lista[i]
            trocou = False
            j = i - distancia
            while j>= 0 and lista[j] > temp:
                lista[j+distancia] = lista[j]
                trocou = True
                j -= distancia
            
            if trocou:
                lista[j+distancia] = temp
            i += 1
        
        distancia = distancia // 2
    
    return lista

lista3 = shell_sort(lista3)
print(lista3)