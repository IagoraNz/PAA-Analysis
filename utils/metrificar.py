import time as t
import sys
import matplotlib.pyplot as plt
from pathlib import Path

arrays_random = [[], [], []]
arrays_C = [[], [], []]
arrays_De = [[], [], []]

# Adiciona o caminho absoluto da pasta 'src' ao sys.path
caminho_src = Path(__file__).parent.parent / "src"
sys.path.append(str(caminho_src))

from gnome import gnomesort
from shell import shell_sort 

def read_array(arquivo, num_linhas=None):
    with open(arquivo, 'r') as f:
        if num_linhas:
            array = [int(linha.strip()) for _, linha in zip(range(num_linhas), f)]
        else:
            array = [int(linha.strip()) for linha in f]
    return array

# Arrays de 15000

for x in range(15000): # Crescente
    arrays_C[0].append(x+1)

for x in range(15000, 0, -1): # Decrescente
    arrays_De[0].append(x)

arrays_random[0] = read_array("array.txt")

# Arrays de 10000

for x in range(10000): # Crescente
    arrays_C[1].append(x+1)

for x in range(10000, 0, -1): # Decrescente
    arrays_De[1].append(x)

arrays_random[1] = read_array("array.txt", 10000)

# Arrays de 5000

for x in range(5000): # Crescente
    arrays_C[2].append(x+1)

for x in range(5000, 0, -1): # Decrescente
    arrays_De[2].append(x)

arrays_random[2] = read_array("array.txt", 5000)


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
    for _ in range(30):
        time, array_sorting = sorting_algorithm(array, function)
        times.append(round(time, 3))

    return times

def plotar_graficos(times, algorithm, ordem):
    # Dados (seus tempos já calculados)
    algoritmos = ['GnomeSort', 'ShellSort']
    tempos = times  # Lista de tempos do GnomeSort

    # Configurações do gráfico
    plt.figure(figsize=(10, 6))  # Tamanho do gráfico

    # Plotando os tempos
    plt.plot(tempos[0], label='15000', marker='o', linestyle='-', color='black')
    plt.plot(tempos[1], label='10000', marker='s', linestyle='--', color='green')
    plt.plot(tempos[2], label='5000', marker='s', linestyle='--', color='blue')

    # Adicionando detalhes ao gráfico
    plt.title(f'Comparação de Tempo de Execução em Diferentes Tamanhos ({algorithm}) - ({ordem})', fontsize=14)
    plt.xlabel('Execução (Nº da Tentativa)', fontsize=12)
    plt.ylabel('Tempo (segundos)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Ajustando os eixos
    plt.xticks(range(30), range(1, 31))  # Rótulos de 1 a 30

    # Mostrando o gráfico
    plt.show()

def plotar_graficos_barra(mediaShell, mediaGnome, ordem):
    # Dados
    tamanhos = ['5000', '10000', '15000']
    algoritmos = ['ShellSort', 'GnomeSort']
    
    # Criando as listas de valores
    valores_shell = [mediaShell[2], mediaShell[1], mediaShell[0]]
    valores_gnome = [mediaGnome[2], mediaGnome[1], mediaGnome[0]]
    
    x = range(len(tamanhos))  # Posições das barras
    largura = 0.4  # Largura das barras
    
    # Criando o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar([i - largura/2 for i in x], valores_shell, width=largura, color='black', label='ShellSort')
    plt.bar([i + largura/2 for i in x], valores_gnome, width=largura, color='blue', label='GnomeSort')
    
    # Adicionando rótulos e título
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo Médio (ms)')
    plt.title(f'Tempos Médios de Ordenação - {ordem}')
    plt.xticks(x, tamanhos)  # Define os rótulos do eixo x
    plt.legend()
    
    # Exibindo valores nas barras
    for i, v in enumerate(valores_shell):
        plt.text(i - largura/2, v + 0.01 * max(valores_shell + valores_gnome), f'{v:.5f}', ha='center', fontsize=12)
    for i, v in enumerate(valores_gnome):
        plt.text(i + largura/2, v + 0.01 * max(valores_shell + valores_gnome), f'{v:.5f}', ha='center', fontsize=12)
    
    # Exibir gráfico
    plt.show()


times_shell = [[], [], []]
times_gnome = [[], [], []]

media_gnome = [0, 0, 0]

media_shell = [0, 0, 0]

times_shell[0] = times_for_30(shell_sort, arrays_random[0])

times_shell[1] = times_for_30(shell_sort, arrays_random[1])

times_shell[2] = times_for_30(shell_sort, arrays_random[2])

plotar_graficos(times_shell, "Shell Sort", "Lista Aleatoria")

times_gnome[0] = times_for_30(gnomesort, arrays_random[0])

times_gnome[1] = times_for_30(gnomesort, arrays_random[1])

times_gnome[2] = times_for_30(gnomesort, arrays_random[2])

plotar_graficos(times_gnome, "Gnome Sort", "Lista Aleatoria")

for x in range(30):
    media_gnome[0] = media_gnome[0] + times_gnome[0][x]
    media_gnome[1] += times_gnome[1][x]
    media_gnome[2] += times_gnome[2][x]
    media_shell[0] += times_shell[0][x]
    media_shell[1] += times_shell[1][x]
    media_shell[2] += times_shell[2][x]

media_gnome[0] = media_gnome[0] / 30
media_gnome[1] = media_gnome[1] / 30
media_gnome[2] = media_gnome[2] / 30

media_shell[0] = media_shell[0] / 30
media_shell[1] = media_shell[1] / 30
media_shell[2] = media_shell[2] / 30

plotar_graficos_barra(media_shell, media_gnome, "Lista Aleatoria")

# ===================================================================

times_shell[0] = times_for_30(shell_sort, arrays_De[0])

times_shell[1] = times_for_30(shell_sort, arrays_De[1])

times_shell[2] = times_for_30(shell_sort, arrays_De[2])

plotar_graficos(times_shell, "Shell Sort", "Decrescente")

times_gnome[0] = times_for_30(gnomesort, arrays_De[0])

times_gnome[1] = times_for_30(gnomesort, arrays_De[1])

times_gnome[2] = times_for_30(gnomesort, arrays_De[2])

plotar_graficos(times_gnome, "Gnome Sort", "Decrescente")

for x in range(30):
    media_gnome[0] = media_gnome[0] + times_gnome[0][x]
    media_gnome[1] += times_gnome[1][x]
    media_gnome[2] += times_gnome[2][x]
    media_shell[0] += times_shell[0][x]
    media_shell[1] += times_shell[1][x]
    media_shell[2] += times_shell[2][x]

media_gnome[0] = media_gnome[0] / 30
media_gnome[1] = media_gnome[1] / 30
media_gnome[2] = media_gnome[2] / 30

media_shell[0] = media_shell[0] / 30
media_shell[1] = media_shell[1] / 30
media_shell[2] = media_shell[2] / 30

plotar_graficos_barra(media_shell, media_gnome, "Decrescente")

# # ===================================================================

times_shell[0] = times_for_30(shell_sort, arrays_C[0])

times_shell[1] = times_for_30(shell_sort, arrays_C[1])

times_shell[2] = times_for_30(shell_sort, arrays_C[2])

plotar_graficos(times_shell, "Shell Sort", "Crescente")


times_gnome[0] = times_for_30(gnomesort, arrays_C[0])

times_gnome[1] = times_for_30(gnomesort, arrays_C[1])

times_gnome[2] = times_for_30(gnomesort, arrays_C[2])

plotar_graficos(times_gnome, "Gnome Sort", "Crescente")

for x in range(30):
    media_gnome[0] = media_gnome[0] + times_gnome[0][x]
    media_gnome[1] += times_gnome[1][x]
    media_gnome[2] += times_gnome[2][x]
    media_shell[0] += times_shell[0][x]
    media_shell[1] += times_shell[1][x]
    media_shell[2] += times_shell[2][x]

media_gnome[0] = media_gnome[0] / 30
media_gnome[1] = media_gnome[1] / 30
media_gnome[2] = media_gnome[2] / 30

media_shell[0] = media_shell[0] / 30
media_shell[1] = media_shell[1] / 30
media_shell[2] = media_shell[2] / 30

plotar_graficos_barra(media_shell, media_gnome, "Crescente")

# # ===================================================================



        
