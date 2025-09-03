from typing import List

def brute_force_d2(dias: List[int]) -> int:
    """
    Varre todas janelas (i..j) acumulando soma incrementalmente -> O(n^2).
    """
    n = len(dias)
    if n == 0:
        return 0
    best = dias[0]
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += dias[j]
            if s > best:
                best = s
    return best
