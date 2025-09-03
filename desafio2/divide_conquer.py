from typing import List

def divide_conquer_d2(dias: List[int]) -> int:
    """
    Máxima soma contígua via Divide & Conquer (O(n log n)).
    """

    def rec(l: int, r: int) -> int:
        if l == r:
            return dias[l]
        m = (l + r) // 2

        left_best = rec(l, m)
        right_best = rec(m + 1, r)

        # melhor sufixo da esquerda
        soma, best_left_suffix = 0, float("-inf")
        for i in range(m, l - 1, -1):
            soma += dias[i]
            best_left_suffix = max(best_left_suffix, soma)

        # melhor prefixo da direita
        soma, best_right_prefix = 0, float("-inf")
        for i in range(m + 1, r + 1):
            soma += dias[i]
            best_right_prefix = max(best_right_prefix, soma)

        cross = best_left_suffix + best_right_prefix
        return max(left_best, right_best, cross)

    return rec(0, len(dias) - 1)
