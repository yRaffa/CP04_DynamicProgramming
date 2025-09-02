# Metodo Brute Force via BitMask para o Desafio 1
# Testa todos os subconjuntos e retorna o maior benefício possível sem ultrapassar o orçamento
# Complexidade: O(2^n * n)
def brute_force_d1(projetos, orcamento):
    n = len(projetos)
    best_beneficio = 0

    for mask in range(1 << n):  # (0 ... 2^n - 1)
        custo = 0
        beneficio = 0
        escolhidos = []
        for i in range(n):
            if mask & (1 << i):
                custo += projetos[i].custo
                beneficio += projetos[i].beneficio
                escolhidos.append(i)
                if custo > orcamento:
                    break
        if custo <= orcamento and beneficio > best_beneficio:
            best_beneficio = beneficio

    return best_beneficio, escolhidos

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