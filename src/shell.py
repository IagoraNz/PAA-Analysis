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


def gaps_tokuda(tamanho):
    gaps = []
    k = 0
    while True:
        gap = (9 * (9 ** k) - 4 * (4 ** k)) // 5
        if gap > tamanho:
            break
        gaps.append(gap)
        k += 1
    return list(reversed(gaps))


def shell_sort(lista):
    gaps = gaps_tokuda(len(lista))

    for distancia in gaps:
        i = distancia
        while i < len(lista):
            temp = lista[i]
            trocou = False
            j = i - distancia
            while j >= 0 and lista[j] > temp:
                lista[j + distancia] = lista[j]
                trocou = True
                j -= distancia

            lista[j + distancia] = temp
            i += 1
    
    return lista

lista3 = shell_sort(lista3)
print(lista3)