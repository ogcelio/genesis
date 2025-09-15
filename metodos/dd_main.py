import numpy as np
from time import perf_counter

from metodos.quadratura.quadratura_backend import quadratura

from metodos.Diamond_Difference.calc_psiM import calc_psiM
from metodos.Diamond_Difference.calc_foward import foward
from metodos.Diamond_Difference.calc_backward import backward
from metodos.Diamond_Difference.calc_ssj import calc_ssj

from metodos.common.calc_fi import calc_fi
from metodos.common.init_variables import init_psiX, init_hj
from metodos.common.calc_dr import calc_dr
from metodos.common.calc_sigmaA import calc_sigmaA
from metodos.common.calc_abs_rate import calc_abs_rate
from metodos.common.calc_escape_rate import calc_escape_rate
from metodos.common.trivial_sol_test import trivial_sol


def diamond_difference(
    sigmaT,
    sigmaS0,
    sigmaS1,
    sigmaS2,
    Qj,
    NiSigmaF,
    N,
    cce,
    ccd,
    prec,
    NN,
    regs,
    n_regs,
    esp_R,
):
    # Coletando tempo inicial
    initial_time = perf_counter()

    ###ETAPA INICIALIZAÇÃO DE VARIÁVEIS

    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    NNT = sum(NN)  # Número total de nodos
    psiX = init_psiX(N, NNT, cce, ccd)  # Fluxos Angulares
    hj = init_hj(NN, n_regs, esp_R)  # Espessura do nodo por região
    iteracao = 0

    if trivial_sol(Qj, cce, ccd, n_regs):
        # Arredondando fi_final
        initial_fi = np.zeros(NNT + 1)

        # Arredondando psiX
        abs_rate = np.zeros(n_regs)
        escape_rate = np.zeros(2)

        # Coletando Tempo final
        final_time = perf_counter()

        # Calculando tempo de execução
        execution_time = abs(final_time - initial_time)
        return (
            initial_fi,
            psiX,
            iteracao,
            abs_rate,
            escape_rate,
            execution_time,
        )  # Caso fontes e condições de contorno sejam nulas, o código retorna os fluxos completamente preenchidos de zeros

    while True:
        iteracao += 1
        ###ETAPA CÁLCULO DOS PSIS MÉDIOS
        psiM = calc_psiM(N, NNT, psiX)

        ###ETAPA CÁLCULO DO Ssj
        Ssj = calc_ssj(N, NN, NNT, regs, psiM, w, sigmaS0)

        ###ETAPA CÁLCULO DO FI INICIAL
        initial_fi = calc_fi(N, NNT, w, psiX)

        ###ETAPA IDA
        psiX = foward(N, NN, NNT, regs, psiX, hj, Ssj, Qj, mi, sigmaT)

        ###ETAPA VOLTA
        psiX = backward(N, NN, NNT, regs, psiX, hj, Ssj, Qj, mi, sigmaT)

        ###ETAPA CÁLCULO DO FI FINAL
        final_fi = calc_fi(N, NNT, w, psiX)

        ###ETAPA CÁLCULO DO DR
        dr = calc_dr(initial_fi, final_fi)
        if dr < prec:
            break

    ###ETAPA ATUALIZAÇÃO DOS PSIS MÉDIOS
    psiM = calc_psiM(N, NNT, psiX)

    ###ETAPA TAXA DE ABSORÇÃO
    # Fi Medio
    average_fi = 2 * calc_fi(N, NNT - 1, w, psiM)

    # Gerando Sigma A
    sigmaA = calc_sigmaA(sigmaT, sigmaS0)

    # Taxa de Absorção
    abs_rate = calc_abs_rate(NN, regs, average_fi, hj, sigmaA)

    ###ETAPA TAXA DE FUGA
    escape_rate = calc_escape_rate(N, psiX, mi, w)

    # Coletando Tempo final
    final_time = perf_counter()

    # Calculando tempo de execução
    execution_time = abs(final_time - initial_time)
    return final_fi, psiX, iteracao, abs_rate, escape_rate, execution_time
