def calc_psi(N, node, psi, aux_em, inv_aux_in, sol_dif, part_sol):
    ###ETAPA CÁLCULO DA MATRIZ AUXILIAR
    aux = aux_em @ inv_aux_in

    ###ETAPA CÁLCULO DO VETOR DOS FLUXOS EMERGENTES
    psi_em = (aux @ sol_dif) + part_sol

    for m in range(N // 2):
        psi[node + 1][m] = psi_em[m]
        psi[node][m + (N // 2)] = psi_em[m + (N // 2)]

    return psi
