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
            j = i - distancia
            while j >= 0 and lista[j] > temp:
                lista[j + distancia] = lista[j]
                j -= distancia

            lista[j + distancia] = temp
            i += 1
    
    return lista
