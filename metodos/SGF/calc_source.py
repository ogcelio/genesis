def calc_source(
    N: int, TOTAL_NODES: int, PART_SOL_DICT: dict, THETA_DICT: dict
) -> dict:
    # CRIANDO O DICT DE FONTES
    source = dict()

    # CRIANDO O VETOR DE FONTE EM UM NODO
    source_vector = ndarray(N)

    # MONTANDO A MATRIZ DE FONTES
    node = 0
    for index_reg, num_nodes in enumerate(NUM_NODES):
        reg = REGS[index_reg] - 1

        # COLETANDO SOLUÇÃO PARTICULAR
        part_sol = PART_SOL_DICT[f"{reg}"]

        for _ in range(num_nodes):
            # COLETANDO THETA
            theta = THETA_DICT[f"{node}"]

            # CALCULANDO A FONTE
            for m in range(N):
            	soma = 0
	        	for n in range(N):
	        		soma += theta[m][n] * part_sol[n]

	        	source_vector[m] = part_sol[m] - soma

	        # COLOCANDO O VETOR DE FONTES NO DICT
	        source.update({f"{node}": source_vector})

            node += 1

    return source
