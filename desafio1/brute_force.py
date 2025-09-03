# Metodo Brute Force via BitMask para o Desafio 1
# Testa todos os subconjuntos e retorna o maior benefício possível sem ultrapassar o orçamento
# Complexidade: O(2^n * n)

from typing import List, Tuple

def brute_force_d1(projetos: List[Tuple[int, int]], orcamento: int) -> int:
    """
    Força bruta via bitmask: testa todos os subconjuntos.
    Retorna o maior benefício possível sem ultrapassar o orçamento.
    """
    n = len(projetos)
    best = 0

    # Para cada subconjunto representado por mask (0 .. 2^n - 1)
    for mask in range(1 << n):
        custo = 0
        beneficio = 0
        # acumula custo/benefício dos itens presentes no mask
        i = 0
        m = mask
        while m:
            if m & 1:
                c, b = projetos[i]
                custo += c
                beneficio += b
                # early break se passar do orçamento (pequima otimização)
                if custo > orcamento:
                    break
            i += 1
            m >>= 1
        else:
            # só atualiza se não quebrou por ultrapassar orçamento
            if custo <= orcamento and beneficio > best:
                best = beneficio

    return best

'''
def brute_force_d1(projetos, orcamento):
    n = len(projetos)
    melhor_beneficio = 0
    escolhidos = []
    for mask in range(1 << n):  # (0 ... 2^n - 1)
        custo, beneficio = 0, 0
        testados = []
        for i in range(n):
            if mask & (1 << i):
                custo += projetos[i].custo
                beneficio += projetos[i].beneficio
                testados.append(i)
                if custo > orcamento:
                    break
        if custo <= orcamento and beneficio > melhor_beneficio:
            melhor_beneficio = beneficio
            escolhidos = testados

    return melhor_beneficio, escolhidos
'''
    
'''
def brute_force_d1(projetos, orcamento):
    n = len(projetos)
    melhor = 0
    for mask in range(1 << n):
        custo = 0
        beneficio = 0
        i = 0
        m = mask
        while m:
            if m & 1:
                c, b = projetos[i]
                custo += c
                beneficio += b
                if custo > orcamento: # Impede o custo de passar o orçamento
                    break
            i += 1
            m >>= 1
        else:
            if custo <= orcamento and beneficio > melhor:
                melhor = beneficio
    return melhor
'''