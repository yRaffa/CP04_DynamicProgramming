from typing import List

def divide_conquer_d2(dias: List[int]) -> int:
    """
    Divide & Conquer: recursivo. Retorna o máximo subarray sum.
    """

    def rec(l: int, r: int) -> int:
        if l == r:
            return dias[l]
        m = (l + r) // 2
        left_best = rec(l, m)
        right_best = rec(m + 1, r)

        # melhor sufixo na esquerda
        s = 0
        best_left_suffix = float('-inf')
        for i in range(m, l - 1, -1):
            s += dias[i]
            if s > best_left_suffix:
                best_left_suffix = s

        # melhor prefixo na direita
        s = 0
        best_right_prefix = float('-inf')
        for i in range(m + 1, r + 1):
            s += dias[i]
            if s > best_right_prefix:
                best_right_prefix = s

        cross = best_left_suffix + best_right_prefix
        return max(left_best, right_best, cross)

    if not dias:
        return 0
    return rec(0, len(dias) - 1)
