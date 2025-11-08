import json
from metodos.med_main import med
from metodos.med_mod_main import med_mod
from metodos.dd_main import diamond_difference
from metodos.rm_main import response_matrix
from metodos.sdm_main import sdm
from metodos.msd_main import msd
import numpy as np
from time import perf_counter


N = 4
cce = 1
ccd = 0
prec = 1e-8
NN = [1, 1, 1, 1]
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

sum_initial = []
for i in range(1000):
    final_fi, psi, iteration, abs_rate, escape_rate, execution_time = med_mod(
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
    sum_initial.append(execution_time)

initial = sum(sum_initial) / 1000
print(initial)

print(50 * "-")

sum_final = []
for i in range(1000):
    final_fi, psi, iteration, abs_rate, escape_rate, execution_time = msd(
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
    sum_final.append(execution_time)

final = sum(sum_final) / 1000
print(final)

print(50 * "-")

print((abs(final - initial) / initial) * 100)
