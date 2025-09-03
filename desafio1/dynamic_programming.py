from typing import List, Tuple

def dynamic_programming_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    """
    Knapsack resolvido com Programação Dinâmica (bottom-up).
    """
    dp = [0] * (orcamento + 1)

    for c, b in projetos:
        if c > orcamento:
            continue
        for w in range(orcamento, c - 1, -1):
            dp[w] = max(dp[w], dp[w - c] + b)

    return max(dp)
