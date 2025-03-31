import time as t

def read_array(arquivo):
    with open(arquivo, 'r') as f:
        array = [int(linha[:-1]) for linha in f.readlines()]
    return array

array = read_array("PAA-Analysis/array.txt")

def sorting_algorithm(array, function):
    inicio = t.time()
    function(array)
    fim = t.time()

    return fim - inicio