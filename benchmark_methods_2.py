import json
from time import perf_counter

import numpy as np

from metodos.dd_main import diamond_difference
from metodos.msd_main import msd
from metodos.rm_main import response_matrix
from metodos.sdm_main import sdm
from metodos.sgf_main import sgf

N = 4
cce = 1
ccd = 0
prec = 1e-8
NN = [1000, 1000, 1000, 1000]
regs = [1, 2, 3, 4]
n_regs = 4
esp_R = [5, 5, 5, 5]

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

print(50 * "-")

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
print("DD:")

indices = [0, 1000, 2000, 3000, 4000]
for i in indices:
    print(f"{i}: {final_fi[i]}")

print(50 * "-")

N = 4
cce = 1
ccd = 0
prec = 1e-8
NN = [10, 10, 10, 10]
regs = [1, 2, 3, 4]
n_regs = 4
esp_R = [5, 5, 5, 5]

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
print("SGF:")
indices = [0, 10, 20, 30, 40]

for i in indices:
    print(f"{i}: {final_fi[i]}")

print(50 * "-")
