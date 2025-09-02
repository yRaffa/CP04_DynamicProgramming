import time
import tracemalloc
import random
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
def gerar_testes_d1(n, custo_min = 2, custo_max = 20, benef_min = 10, benef_max = 120):
    projetos = [(random.randint(custo_min, custo_max),
                 random.randint(benef_min, benef_max)) for _ in range(n)]
    return projetos

# Função para gerar aleatóreamente os teste para o desafio 2
def gerar_testes_d2(n, valor_min = -10, valor_max = 10):
    dias = [random.randint(valor_min, valor_max) for _ in range(n)]
    return dias

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
    