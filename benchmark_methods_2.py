# IMPORTANDO BIBLIOTECAS NECESSARIAS
import json
from time import perf_counter

import numpy as np

from metodos.dd_main import diamond_difference
from metodos.msd_main import msd
from metodos.rm_main import response_matrix
from metodos.sdm_main import sdm
from metodos.sgf_main import sgf

# DEFININDO PARAMETROS DO PROBLEMA
N = 4
cce = 1
ccd = 0
prec = 1e-8
regs = [1, 2, 3, 4]
n_regs = 4
esp_R = [5, 5, 5, 5]

# IMPORTANDO DADOS DAS ZONAS MATERIAIS
with open("benchmark_data.json", "r", encoding="utf8") as file:
    propriedades_1grupo = json.load(file)

sigmaT = propriedades_1grupo["sigmaT"]
sigmaS0 = propriedades_1grupo["sigmaS0"]
sigmaS1 = propriedades_1grupo["sigmaS1"]
sigmaS2 = propriedades_1grupo["sigmaS2"]
Qj = propriedades_1grupo["Qj"]
NiSigmaF = propriedades_1grupo["NiSigmaF"]

for i in range(len(sigmaT)):
    sigmaT[i] = float(sigmaT[i])
    sigmaS0[i] = float(sigmaS0[i])
    sigmaS1[i] = float(sigmaS1[i])
    sigmaS2[i] = float(sigmaS2[i])
    Qj[i] = float(Qj[i])
    NiSigmaF[i] = float(NiSigmaF[i])


# FUNCAO PARA PRINTAR RESULTADOS
def print_result(n_regs, esp_r, final_fi):
    for i in range(n_regs + 1):
        print(f"X = {sum(esp_r[:i])}: {final_fi[sum(NN[:i])]}")


print(50 * "-")

# NUMERO DE NODOS PARA O DD
NN = [100, 100, 100, 100]

# EXECUTANDO O DD
final_fi, psi, iteration, abs_rate, escape_rate, execution_time = diamond_difference(
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
)

# PRINTANDO RESULTADOS
print("DD:")
print_result(n_regs, esp_R, final_fi)

print(50 * "-")

# NUMERO DE NODOS PARA O SGF
NN = [10, 10, 10, 10]

# EXECUTANDO O SGF
final_fi, psi, iteration, abs_rate, escape_rate, execution_time = sgf(
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
)

# PRINTANDO RESULTADOS
print("SGF:")
print_result(n_regs, esp_R, final_fi)

print(50 * "-")
