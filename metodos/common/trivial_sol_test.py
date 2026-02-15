from numpy import ndarray


def trivial_sol(Q: list[float] | ndarray, CCE: float, CCD: float) -> bool:
    for source in Q:  # testando se todas as fontes são 0
        if source != 0:
            break
    else:  # se todas as fontes forem 0:
        if CCE == 0 and CCD == 0:
            return True
    return False
