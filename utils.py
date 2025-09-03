import time
import tracemalloc
import random
import numpy as np
import matplotlib.pyplot as plt

# Decorator para medir tempo de execução
def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter() # Marca o tempo de início
        resultado = func(*args, **kwargs) # Chama a função original
        fim = time.perf_counter() # Marca o fim da medição
        tempo = 1000 * (fim - inicio) # Calcula e converte o tempo decorrido para ms
        return {'resultado' : resultado, 'tempo' : tempo} # Retorna o resultado da função original
    return wrapper

# Decorator para medir uso de memória
def medir_memoria(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start() # Inicia o rastreamento de alocação de memória
        resultado = func(*args, **kwargs) # Chama a função original
        memoria = tracemalloc.get_traced_memory() # Obtém a memória atual e o pico de uso
        tracemalloc.stop() # Termina o rastreamento de alocação de memória
        memoria = memoria[1] / 1024 # Converte o pico de memória para KB
        return {'resultado' : resultado, 'memoria' : memoria} # Retorna o resultado da função original
    return wrapper

# Função para gerar aleatóreamente os teste para o desafio 1
def gerar_testes_d1(n, custo_min = 2, custo_max = 20, beneficio_min = 10, beneficio_max = 120):
    projetos = [(random.randint(custo_min, custo_max), random.randint(beneficio_min, beneficio_max)) for _ in range(n)]
    return projetos

# Função para gerar aleatóreamente os teste para o desafio 2
def gerar_testes_d2(n, valor_min = -10, valor_max = 10):
    dias = [random.randint(valor_min, valor_max) for _ in range(n)]
    return dias

'''
# Função para plotar gráficos de tempo de execução
def grafico_tempo(df, titulo):
    plt.figure(figsize = (8,5))
    for coluna in df.columns:
        if coluna != 'n':
            plt.plot(df['n'], df[coluna], marker = 'o', label = coluna)
    plt.title(titulo)
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo de execução (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para plotar gráficos de uso de memória
def grafico_memoria(df, titulo):
    plt.figure(figsize = (8,5))
    for coluna in df.columns:
        if coluna != 'n':
            plt.plot(df['n'], df[coluna], marker = 'o', label = coluna)
    plt.title(titulo)
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Uso de Memória (KB)')
    plt.legend()
    plt.grid(True)
    plt.show()
'''

def grafico_tempo(df, titulo):
    plt.figure(figsize=(10,6))
    for metodo, cor, marcador in zip(
        ["Brute Force (Tempo)", "Divide & Conquer (Tempo)", "Dynamic Programming (Tempo)"],
        ["#d62728", "#1f77b4", "#2ca02c"],  # cores: vermelho, azul, verde
        ["o", "s", "D"]  # circulo, quadrado, diamante
    ):
        plt.plot(df["n"], df[metodo], marker=marcador, linewidth=2.5, markersize=8, color=cor, label=metodo)
        for x, y in zip(df["n"], df[metodo]):
            plt.text(x, y, f"{y:.2f}", fontsize=8, ha="center", va="bottom")

    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo de execução (ms)")
    plt.yscale("log")  # log para destacar diferenças grandes
    plt.title(titulo)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()


def grafico_memoria(df, titulo):
    plt.figure(figsize=(10,6))
    for metodo, cor, estilo in zip(
        ["Brute Force (Memória)", "Divide & Conquer (Memória)", "Dynamic Programming (Memória)"],
        ["#ff7f0e", "#9467bd", "#8c564b"],  # cores laranja, roxo, marrom
        ["--", "-.", ":"]
    ):
        plt.plot(df["n"], df[metodo], linestyle=estilo, linewidth=2.5, marker="o", markersize=6, color=cor, label=metodo)
        plt.fill_between(df["n"], df[metodo], alpha=0.15, color=cor)

    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Uso de memória (KB)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

def grafico_comparativo(df, titulo, metrica="Tempo"):
    x = np.arange(len(df["n"]))
    largura = 0.25

    plt.figure(figsize=(12,6))
    plt.bar(x - largura, df[f"Brute Force ({metrica})"], width=largura, color="#d62728", label="Brute Force")
    plt.bar(x, df[f"Divide & Conquer ({metrica})"], width=largura, color="#1f77b4", label="Divide & Conquer")
    plt.bar(x + largura, df[f"Dynamic Programming ({metrica})"], width=largura, color="#2ca02c", label="Dynamic Programming")

    plt.xticks(x, df["n"])
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel(f"{metrica}")
    plt.title(f"{titulo} - {metrica}")
    plt.legend()
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.show()
