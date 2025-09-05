from typing import List

# Metodo Dynamic Programming para o Desafio 2
# Divide o conjunto pela metade, e combina subconjuntos (custo, beneficio) via busca binaria
# Complexidade: Tempo: O(n), Memoria: O(1)
def dynamic_programming_d2(dias: List[int]) -> int:
    melhor_soma_atual = dias[0]
    melhor_soma_global = dias[0]
    for elemento in dias[1:]:
        melhor_soma_atual = max(elemento, melhor_soma_atual + elemento)
        melhor_soma_global = max(melhor_soma_global, melhor_soma_atual)
    return melhor_soma_global
