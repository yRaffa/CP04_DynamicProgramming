from typing import List

def dynamic_programming_d2(dias: List[int]) -> int:
    """
    Kadane: passa única. best_end = melhor soma terminando no índice atual.
    """
    if not dias:
        return 0
    best_end = dias[0]
    best_so_far = dias[0]
    for x in dias[1:]:
        best_end = x if x > best_end + x else best_end + x
        if best_end > best_so_far:
            best_so_far = best_end
    return best_so_far
