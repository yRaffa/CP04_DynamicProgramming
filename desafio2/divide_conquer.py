from typing import List

# Metodo Divide & Conquer para o Desafio 2
# Calcula qual o melhor subconjunto, e retorna o valor maximo dentro deles
# Complexidade: Tempo: O(n log n), Memoria: O(log n)
def divide_conquer_d2(dias: List[int]) -> int:
    def rec(e: int, d: int) -> int:
        if e == d:
            return dias[e]
        meio_intervalo = (e + d) // 2

        melhor_esquerda = rec(e, meio_intervalo)
        melhor_direita = rec(meio_intervalo + 1, d)

        # melhor sufixo da esquerda
        soma, melhor_esquerda_sufixo = 0, float('-inf')
        for i in range(meio_intervalo, e - 1, -1):
            soma += dias[i]
            melhor_esquerda_sufixo = max(melhor_esquerda_sufixo, soma)

        # melhor prefixo da direita
        soma, melhor_direita_prefixo = 0, float('-inf')
        for i in range(meio_intervalo + 1, d + 1):
            soma += dias[i]
            melhor_direita_prefixo = max(melhor_direita_prefixo, soma)

        combinacao = melhor_esquerda_sufixo + melhor_direita_prefixo
        return max(melhor_esquerda, melhor_direita, combinacao)

    return rec(0, len(dias) - 1)
