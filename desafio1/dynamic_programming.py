from typing import List, Tuple

def dynamic_programming_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    """
    Programação Dinâmica (1D) para 0/1 Knapsack.
    dp[w] = melhor benefício com custo máximo w.
    Atualizamos de trás pra frente para não reutilizar item.
    """
    dp = [0] * (orcamento + 1)
    for c, b in projetos:
        if c > orcamento:
            continue
        for w in range(orcamento, c - 1, -1):
            nova = dp[w - c] + b
            if nova > dp[w]:
                dp[w] = nova
    return max(dp)
