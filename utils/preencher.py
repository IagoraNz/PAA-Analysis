import random

def gerar_numeros_aleatorios(arquivo, quantidade, limite_inferior=0, limite_superior=1000000):
    with open(arquivo, 'w') as f:
        for _ in range(quantidade):
            f.write(f"{random.randint(limite_inferior, limite_superior)}\n")

gerar_numeros_aleatorios("array.txt", 15000, 0, 15000)