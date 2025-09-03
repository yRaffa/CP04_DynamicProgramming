from typing import List

def dynamic_programming_d2(dias: List[int]) -> int:
    """
    Máxima soma contígua via Kadane (Programação Dinâmica, O(n)).
    """
    best_end = dias[0]
    best_so_far = dias[0]

    for x in dias[1:]:
        best_end = max(x, best_end + x)
        best_so_far = max(best_so_far, best_end)

    return best_so_far
