from time import perf_counter

from numpy import zeros

from metodos.common.calc_abs_rate import calc_abs_rate
from metodos.common.calc_dr import calc_dr
from metodos.common.calc_escape_rate import calc_escape_rate
from metodos.common.calc_fi import calc_fi
from metodos.common.calc_sigmaA import calc_sigmaA
from metodos.common.init_variables import init_C0j, init_hj, init_psiX
from metodos.common.trivial_sol_test import trivial_sol
from metodos.quadratura.quadratura_backend import quadratura
from metodos.SDM.calc_eigen import calc_eigen
from metodos.SDM.calc_part_sol import calc_part_sol
from metodos.SGF.calc_psi import backward, foward
from metodos.SGF.calc_source import calc_source
from metodos.SGF.calc_sweep_matrices import calc_sweep_matrices
from metodos.SGF.calc_theta import calc_theta


def sgf(
    SIGMA_T,
    SIGMA_S0,
    SIGMA_S1,
    SIGMA_S2,
    Q,
    NI_SIGMA_F,
    N,
    CCE,
    CCD,
    PREC,
    NUM_NODES,
    REGS,
    NUM_REGS,
    ESP_REGS,
):
    # COLETANDO TEMPO INICIAL
    INITIAL_TIME = perf_counter()

    # INICIALIZANDO VARIÁVEIS
    MI, W = quadratura(N)
    TOTAL_NODES = sum(NUM_NODES)
    psi = init_psiX(N, TOTAL_NODES, CCE, CCD)
    H = init_hj(NUM_NODES, NUM_REGS, ESP_REGS)
    C0 = init_C0j(SIGMA_T, SIGMA_S0)
    psiM = zeros((TOTAL_NODES, N))
    iteration = 0

    if trivial_sol(Q, CCE, CCD, NUM_REGS):
        initial_fi = zeros(TOTAL_NODES + 1)

        abs_rate = zeros(NUM_REGS)
        escape_rate = zeros(2)

        # Coletando Tempo final
        FINAL_TIME = perf_counter()

        # Calculando tempo de execução
        execution_time = abs(FINAL_TIME - INITIAL_TIME)
        return (
            initial_fi,
            psi,
            iteration,
            abs_rate,
            escape_rate,
            execution_time,
        )  # Caso fontes e condições de contorno sejam nulas, o código retorna os fluxos completamente preenchidos de zeros

    # CALCULANDO AUTOVALORES E AUTOVETORES
    EIGEN_DICT = calc_eigen(N, REGS, MI, W, C0)

    # CALCULANDO SOLUÇÕES PARTICULARES
    PART_SOL_DICT = calc_part_sol(N, Q, REGS, SIGMA_T, SIGMA_S0, W)

    # CALCULANDO THETAS
    THETA_DICT = calc_theta(N, H, SIGMA_T, REGS, EIGEN_DICT)

    # CALCULANDO FONTES
    SOURCE_DICT = calc_source(N, REGS, PART_SOL_DICT, THETA_DICT)

    # CALCULANDO MATRIZES GP, GM, K
    GP_DICT, GM_DICT, K_DICT = calc_sweep_matrices(
        N, H, Q, MI, W, REGS, SIGMA_T, SIGMA_S0, THETA_DICT, SOURCE_DICT
    )

    while True:
        iteration += 1

        # CÁLCULO DO FLUXO ESCALAR INICIAL
        initial_fi = calc_fi(N, TOTAL_NODES, W, psi)

        # INICIANDO PROCESSO ITERATIVO DE IDA
        node = 1
        for index_reg, num_nodes in enumerate(NUM_NODES):
            gp = GP_DICT[f"{index_reg}"]
            gm = GM_DICT[f"{index_reg}"]
            k = K_DICT[f"{index_reg}"]

            for j in range(num_nodes):
                foward(N, gp, gm, k, psi, node)
                node += 1

        # INICIANDO PROCESSO ITERATIVO DE VOLTA
        node = TOTAL_NODES - 1
        for index_reg, num_nodes in reversed(tuple(enumerate(NUM_NODES))):
            gp = GP_DICT[f"{index_reg}"]
            gm = GM_DICT[f"{index_reg}"]
            k = K_DICT[f"{index_reg}"]

            for j in range(num_nodes):
                backward(N, gp, gm, k, psi, node)
                node -= 1

        # CÁLCULO DO FLUXO ESCALAR FINAL
        final_fi = calc_fi(N, TOTAL_NODES, W, psi)

        # SDM CONVERGE EM UMA ITERAÇÃO NESSAS CONDIÇÕES
        if iteration == 1 and NUM_REGS == 1 and TOTAL_NODES == 1:
            break

        # CÁLCULO DO DR
        dr = calc_dr(initial_fi, final_fi)
        if dr < PREC:
            break

    # TAXA DE ABSORÇÃO

    # FLUXO ESCALAR MÉDIO
    average_fi = 2 * calc_fi(N, TOTAL_NODES - 1, W, psiM)

    # CALCULANDO SIGMA_A
    SIGMA_A = calc_sigmaA(SIGMA_T, SIGMA_S0)

    # CALCULANDO TAXA DE ABSORÇÃO
    abs_rate = calc_abs_rate(NUM_NODES, REGS, average_fi, H, SIGMA_A)

    # TAXA DE FUGA
    escape_rate = calc_escape_rate(N, psi, MI, W)

    # COLETANDO TEMPO FINAL
    FINAL_TIME = perf_counter()

    # CALCULANDO O TEMPO DE EXECUÇÃO
    execution_time = abs(FINAL_TIME - INITIAL_TIME)

    return final_fi, psi, iteration, abs_rate, escape_rate, execution_time
