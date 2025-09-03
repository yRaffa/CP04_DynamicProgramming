from typing import List, Tuple
import bisect

def _subsets(items: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """Gera todos os pares (custo, beneficio) de subconjuntos."""
    res = []
    n = len(items)
    for mask in range(1 << n):
        custo, benef = 0, 0
        for i in range(n):
            if mask & (1 << i):
                c, b = items[i]
                custo += c
                benef += b
        res.append((custo, benef))
    return res

def divide_conquer_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    """
    Knapsack com abordagem Meet-in-the-Middle (Divide & Conquer).
    Divide em duas metades, gera todos subconjuntos e combina via busca binária.
    """
    n = len(projetos)
    mid = n // 2
    A = projetos[:mid]
    B = projetos[mid:]

    SA = _subsets(A)
    SB = _subsets(B)

    # Ordena SB por custo e remove combinações dominadas
    SB.sort(key=lambda x: (x[0], -x[1]))
    filtered = []
    max_b = -1
    for c, b in SB:
        if b > max_b:
            filtered.append((c, b))
            max_b = b

    costsB = [c for c, _ in filtered]
    benefitsB = [b for _, b in filtered]

    best = 0
    for ca, ba in SA:
        restante = orcamento - ca
        if restante < 0:
            continue
        idx = bisect.bisect_right(costsB, restante) - 1
        if idx >= 0:
            best = max(best, ba + benefitsB[idx])

    return best
