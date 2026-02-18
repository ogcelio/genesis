def trivial_sol(Q: list[float], REGS: list[int], CCE: float, CCD: float) -> bool:
    if CCE != 0 or CCD != 0:  # testando se as condções de contorno são 0
        return False

    for reg in REGS:  # testando se todas as fontes são 0
        if Q[reg - 1] != 0:
            return False

    return True
