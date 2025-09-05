from typing import List, Tuple
import bisect

# Gera todos os pares (custo, beneficio) de subconjuntos
def _subsets(itens: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    n = len(itens)
    resultado = []
    for mask in range(1 << n):
        custo, beneficio = 0, 0
        for i in range(n):
            if mask & (1 << i):
                c, b = itens[i]
                custo += c
                beneficio += b
        resultado.append((custo, beneficio))
    return resultado

# Metodo Divide & Conquer para o Desafio 1
# Divide o conjunto pela metade, e combina subconjuntos (custo, beneficio) via busca binaria
# Complexidade: Tempo: O(2^(n/2) * n), Memoria: O(2^(n/2))
def divide_conquer_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    n = len(projetos)
    metade = n // 2
    projetos_A = projetos[:metade]
    projetos_B = projetos[metade:]
    subconjuntos_A = _subsets(projetos_A)
    subconjuntos_B = _subsets(projetos_B)
    subconjuntos_B.sort(key = lambda x: (x[0], -x[1])) # Ordena subconjuntos_B por custo e remove combinações dominadas, mantem uma sequência onde o benefício é não decrescente com o custo
    filtrados = []
    maximo_B = -1
    for cB, bB in subconjuntos_B:
        if bB > maximo_B:
            filtrados.append((cB, bB))
            maximo_B = bB
    custos_B = [cB for cB, _ in filtrados]
    beneficios_B = [bB for _, bB in filtrados]
    melhor = 0
    for cA, bA in subconjuntos_A:
        restante = orcamento - cA
        if restante < 0:
            continue
        index = bisect.bisect_right(custos_B, restante) - 1
        if index >= 0:
            melhor = max(melhor, bA + beneficios_B[index])
    return melhor
