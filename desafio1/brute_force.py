from typing import List, Tuple

# Metodo Brute Force via BitMask para o Desafio 1
# Testa todos os subconjuntos e retorna o maior benefício possível sem ultrapassar o orçamento
# Complexidade: O(2^n * n)
def brute_force_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    n = len(projetos)
    melhor_beneficio = 0
    for mask in range(1 << n):
        custo, beneficio = 0, 0
        for i in range(n):
            if mask & (1 << i):
                c, b = projetos[i]
                custo += c
                beneficio += b
        if custo <= orcamento:
            melhor_beneficio = max(melhor_beneficio, beneficio)
    return melhor_beneficio