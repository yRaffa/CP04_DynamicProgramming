def divide_conquer_d1(projetos, orcamento):
    n = len(projetos)
    melhor_beneficio = 0
    escolhidos = []
    def dc(i, orcamento_rest):
        if i == n:
            return 0, []
        custo_sem_i, beneficio_sem_i = dc(i+1, orcamento_rest)
        custo_com_i, beneficio_com_i = 0, []
    return melhor_beneficio, escolhidos