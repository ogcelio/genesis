from numpy import zeros


def calc_source(N: int, REGS: list, PART_SOL_DICT: dict, THETA_DICT: dict) -> dict:
    # CRIANDO O DICT DE FONTES
    source = dict()

    # CRIANDO O VETOR DE FONTE EM UM NODO
    source_vector = zeros(N)

    # MONTANDO A MATRIZ DE FONTES
    for index_reg, reg in enumerate(REGS):
        # COLETANDO SOLUÇÃO PARTICULAR
        part_sol = PART_SOL_DICT[f"{index_reg}"]

        # COLETANDO THETA
        theta = THETA_DICT[f"{index_reg}"]

        # CALCULANDO A FONTE
        for m in range(N):
            soma = 0
            for n in range(N):
                soma += theta[m][n] * part_sol[n]

            source_vector[m] = part_sol[m] - soma

        # COLOCANDO O VETOR DE FONTES NO DICT
        source.update({f"{index_reg}": source_vector})

    return source
