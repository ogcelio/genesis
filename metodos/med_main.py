import numpy as np
from time import perf_counter

from metodos.quadratura.quadratura_backend import quadratura

from metodos.MED.calc_psiM import calc_psiM
from metodos.MED.calc_psiX import calc_psiX
from metodos.MED.calc_eigen import calc_eigen
from metodos.MED.calc_part_sol import calc_part_sol
from metodos.MED.calc_alfa import calc_alfa

from metodos.common.calc_fi import calc_fi
from metodos.common.init_variables import init_psiX, init_hj, init_C0j
from metodos.common.calc_dr import calc_dr
from metodos.common.calc_sigmaA import calc_sigmaA
from metodos.common.calc_abs_rate import calc_abs_rate
from metodos.common.calc_escape_rate import calc_escape_rate
from metodos.common.trivial_sol_test import trivial_sol


def med(
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

    ###ETAPA INICIALIZANDO VARIÁVEIS
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    NNT = sum(NN)  # Número total de nodos
    psiX = init_psiX(N, NNT, cce, ccd)  # Fluxos Angulares
    hj = init_hj(NN, n_regs, esp_R)  # Espessura do nodo por região
    C0j = init_C0j(sigmaT, sigmaS0)
    psiM = np.zeros((NNT, N))
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
        ###ETAPA CÁLCULO DO FI INICIAL
        initial_fi = calc_fi(N, NNT, w, psiX)

        # REALIZANDO O MESMO PROCESSO PARA CADA NODO
        reg = regs[0] - 1
        contador = 0
        k = 0
        for node in range(NNT):
            if contador == NN[k]:
                k += 1
                reg = regs[k] - 1
                contador = 0

            ###ETAPA CÁLCULO DE AUTOVALORES E AUTOVETORES
            eigenvalues, eigenvectors = calc_eigen(N, reg, mi, w, C0j)

            ###ETAPA CÁLCULO DA SOLUÇÃO PARTICULAR
            part_sol = calc_part_sol(N, Qj, reg, sigmaT, sigmaS0, w)

            ###ETAPA CÁLCULO DO VETOR SOLUÇÃO PARA OS ALFAS
            alfa = calc_alfa(
                N, hj, eigenvalues, eigenvectors, sigmaT, reg, k, node, psiX, part_sol
            )

            ###ETAPA ATUALIZANDO PSIS
            psiX = calc_psiX(
                N,
                hj,
                alfa,
                part_sol,
                eigenvalues,
                eigenvectors,
                sigmaT,
                node,
                reg,
                k,
                psiX,
            )

            ###ETAPA ATUALIZANDO PSIS MÉDIOS
            psiM = calc_psiM(
                N,
                hj,
                alfa,
                part_sol,
                eigenvalues,
                eigenvectors,
                sigmaT,
                node,
                reg,
                k,
                psiM,
            )

            ###ETAPA CÁLCULO DO FI FINAL
            final_fi = calc_fi(N, NNT, w, psiX)

            contador += 1

        if iteracao == 1 and n_regs == 1 and NNT == 1:
            break

        ###ETAPA CÁLCULO DO DR
        dr = calc_dr(initial_fi, final_fi)
        if dr < prec:
            break

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
