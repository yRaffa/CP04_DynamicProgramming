from .brute_force import brute_force_d2
from .divide_conquer import divide_conquer_d2
from .dynamic_programming import dynamic_programming_d2
from utils import medir_tempo, medir_memoria

# Funções para medir tempo e memória do metodo Brute Force do Desafio 2
@medir_tempo
def tempo_brute_force(dias):
    return brute_force_d2(dias)
@medir_memoria
def memoria_brute_force(dias):
    return brute_force_d2(dias)

# Funções para medir tempo e memória do metodo Divide & Conquer do Desafio 2
@medir_tempo
def tempo_divide_conquer(dias):
    return divide_conquer_d2(dias)
@medir_memoria
def memoria_divide_conquer(dias):
    return divide_conquer_d2(dias)

# Funções para medir tempo e memória do metodo Dynamic Programming do Desafio 2
@medir_tempo
def tempo_dynamic_programming(dias):
    return dynamic_programming_d2(dias)
@medir_memoria
def memoria_dynamic_programming(dias):
    return dynamic_programming_d2(dias)

def executar_d2(dias):
    n = len(dias)
    resultados = {
        "n": n
    }
    # Brute Force
    tempo = tempo_brute_force(dias)['tempo']
    memoria = memoria_brute_force(dias)['memoria']
    resultados['Brute Force (Tempo)'] = tempo
    resultados['Brute Force (Memória)'] = memoria
    # Divide & Conquer
    tempo = tempo_divide_conquer(dias)['tempo']
    memoria = memoria_divide_conquer(dias)['memoria']
    resultados['Divide & Conquer (Tempo)'] = tempo
    resultados['Divide & Conquer (Memória)'] = memoria
    # Dynamic Programming
    tempo = tempo_dynamic_programming(dias)['tempo']
    memoria = memoria_dynamic_programming(dias)['memoria']
    resultados['Dynamic Programming (Tempo)'] = tempo
    resultados['Dynamic Programming (Memória)'] = memoria
    return resultados
