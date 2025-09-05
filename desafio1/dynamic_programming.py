from typing import List, Tuple

# Metodo Dynamic Programming para o Desafio 1
# Divide o conjunto pela metade, e combina subconjuntos (custo, beneficio) via busca binaria
# Complexidade: Tempo: O(n * orcamento), Memoria: O(orcamento)
def dynamic_programming_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    dp = [0] * (orcamento + 1)
    for c, b in projetos:
        if c > orcamento:
            continue
        for w in range(orcamento, c - 1, -1):
            dp[w] = max(dp[w], dp[w - c] + b)
    return max(dp)
