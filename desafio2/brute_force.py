from typing import List

def brute_force_d2(dias: List[int]) -> int:
    """
    Máxima soma contígua via força bruta O(n^2).
    Testa todas as janelas possíveis acumulando soma.
    """
    n = len(dias)
    best = dias[0]
    for i in range(n):
        soma = 0
        for j in range(i, n):
            soma += dias[j]
            best = max(best, soma)
    return best
