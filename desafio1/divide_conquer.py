from typing import List, Tuple
import bisect

def _subsets(items: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """Gera todos os pares (custo, beneficio) para todos os subconjuntos de items."""
    res = []
    n = len(items)
    for mask in range(1 << n):
        custo = 0
        benef = 0
        i = 0
        m = mask
        while m:
            if m & 1:
                c, b = items[i]
                custo += c
                benef += b
            i += 1
            m >>= 1
        res.append((custo, benef))
    return res

def divide_conquer_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    """
    Meet-in-the-middle:
    - divide em A e B
    - gera todos subconjuntos de cada metade
    - para B faz prune (mantém pares com custo crescente e benefício máximo até ali)
    - para cada par em A busca melhor par em B com custo <= restante via bisect
    """
    n = len(projetos)
    mid = n // 2
    A = projetos[:mid]
    B = projetos[mid:]

    SA = _subsets(A)  # (custo, beneficio)
    SB = _subsets(B)

    # Ordena SB por custo e faz pruning (manter somente combinações com benefício crescente)
    SB.sort(key=lambda x: (x[0], -x[1]))  # por custo asc, benefício desc para estabilidade
    filtered = []
    max_b = -1
    for c, b in SB:
        if b > max_b:
            filtered.append((c, b))
            max_b = b
    # Arrays separados para busca binária
    costsB = [c for c, _ in filtered]
    bestB = [b for _, b in filtered]  # já prefix-max por construção

    best = 0
    for ca, ba in SA:
        restante = orcamento - ca
        if restante < 0:
            continue
        # acha índice de maior custo <= restante
        idx = bisect.bisect_right(costsB, restante) - 1
        if idx >= 0:
            candidate = ba + bestB[idx]
        else:
            candidate = ba  # só A
        if candidate > best:
            best = candidate

    return best
