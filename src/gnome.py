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
            