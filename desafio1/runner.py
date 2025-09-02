from .brute_force import brute_force_d1
from .divide_conquer import divide_conquer_d1
from .dynamic_programming import dynamic_programming_d1
from utils import medir_tempo, medir_memoria

# Funções para medir tempo e memória do metodo Brute Force do Desafio 1
@medir_tempo
def tempo_brute_force(projetos, orcamento):
    return brute_force_d1(projetos, orcamento)
@medir_memoria
def memoria_brute_force(projetos, orcamento):
    return brute_force_d1(projetos, orcamento)

# Funções para medir tempo e memória do metodo Divide & Conquer do Desafio 1
@medir_tempo
def tempo_divide_conquer(projetos, orcamento):
    return divide_conquer_d1(projetos, orcamento)
@medir_memoria
def memoria_divide_conquer(projetos, orcamento):
    return divide_conquer_d1(projetos, orcamento)

# Funções para medir tempo e memória do metodo Dynamic Programming do Desafio 1
@medir_tempo
def tempo_dynamic_programming(projetos, orcamento):
    return dynamic_programming_d1(projetos, orcamento)
@medir_memoria
def memoria_dynamic_programming(projetos, orcamento):
    return dynamic_programming_d1(projetos, orcamento)

def executar_d1(projetos, orcamento):
    resultados = {}
    # Brute Force
    tempo = tempo_brute_force(projetos, orcamento)['tempo']
    memoria = memoria_brute_force(projetos, orcamento)['memoria']
    resultados['Brute Force (Tempo)'] = tempo
    resultados['Brute Force (Memória)'] = memoria
    # Divide & Conquer
    tempo = tempo_divide_conquer(projetos, orcamento)['tempo']
    memoria = memoria_divide_conquer(projetos, orcamento)['memoria']
    resultados['Divide & Conquer (Tempo)'] = tempo
    resultados['Divide & Conquer (Memória)'] = memoria
    # Dynamic Programming
    tempo = tempo_dynamic_programming(projetos, orcamento)['tempo']
    memoria = memoria_dynamic_programming(projetos, orcamento)['memoria']
    resultados['Dynamic Programming (Tempo)'] = tempo
    resultados['Dynamic Programming (Memória)'] = memoria
    return resultados
