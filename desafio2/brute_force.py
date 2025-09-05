from typing import List

# Metodo Brute Force via BitMask para o Desafio 2
# Testa todos os subconjuntos e acumula a soma incremental de dias retorna o maior elemento (dias)
# Complexidade: Tempo: O(n^2), Memoria: O(1)
def brute_force_d2(dias: List[int]) -> int:
    n = len(dias)
    melhor_dia = dias[0]
    for i in range(n):
        soma = 0
        for j in range(i, n):
            soma += dias[j]
            melhor_dia = max(melhor_dia, soma)
    return melhor_dia
