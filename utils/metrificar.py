import time as t
import sys
import matplotlib.pyplot as plt
from pathlib import Path

# Adiciona o caminho absoluto da pasta 'src' ao sys.path
caminho_src = Path(__file__).parent.parent / "src"
sys.path.append(str(caminho_src))

from gnome import gnomesort
from shell import shell_sort 

def read_array(arquivo):
    with open(arquivo, 'r') as f:
        array = [int(linha[:-1]) for linha in f.readlines()]
    return array

array_random = read_array("array.txt")

array_C = []

array_De = []

for x in range(10000): # Crescente
    array_C.append(x+1)

for x in range(10000, 0, -1): # Decrescente
    array_De.append(x)

def sorting_algorithm(array, function):
    
    array_sorting = []
    
    inicio = t.time()
    array_sorting = function(array.copy())
    fim = t.time()

    time = fim - inicio

    return time, array_sorting

def times_for_30(function, array):
    times = []
    array_sorting = []
    for _ in range(5):
        time, array_sorting = sorting_algorithm(array, function)
        times.append(round(time, 3))

    return times

def plotar_graficos(times_gnome, times_shell, ordem):
    # Dados (seus tempos já calculados)
    algoritmos = ['GnomeSort', 'ShellSort']
    tempos_gnome = times_gnome  # Lista de tempos do GnomeSort
    tempos_shell = times_shell  # Lista de tempos do ShellSort

    # Configurações do gráfico
    plt.figure(figsize=(10, 6))  # Tamanho do gráfico

    # Plotando os tempos
    plt.plot(tempos_gnome, label='GnomeSort', marker='o', linestyle='-', color='red')
    plt.plot(tempos_shell, label='ShellSort', marker='s', linestyle='--', color='blue')

    # Adicionando detalhes ao gráfico
    plt.title(f'Comparação de Tempo de Execução: GnomeSort vs ShellSort ({ordem})', fontsize=14)
    plt.xlabel('Execução (Nº da Tentativa)', fontsize=12)
    plt.ylabel('Tempo (segundos)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Ajustando os eixos
    plt.xticks(range(30), range(1, 31))  # Rótulos de 1 a 30

    # Mostrando o gráfico
    plt.show()

times_shell = []
times_gnome = []

times_gnome = times_for_30(gnomesort, array_random)
times_shell = times_for_30(shell_sort, array_random)

plotar_graficos(times_gnome, times_shell, "Lista Aleatoria")

times_gnome = times_for_30(gnomesort, array_De)
times_shel = times_for_30(shell_sort, array_De)

plotar_graficos(times_gnome, times_shell, "Lista Decrescente")

times_gnome = times_for_30(gnomesort, array_C)
times_shel = times_for_30(shell_sort, array_C)

plotar_graficos(times_gnome, times_shell, "Lista Crescente")
        
