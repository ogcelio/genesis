import json
from metodos.med_main import med
from metodos.med_mod_main import med_mod
from metodos.dd_main import diamond_difference
from metodos.rm_main import response_matrix
import numpy as np
from time import perf_counter


""" N = 4
cce = 1
ccd = 0
prec = 1e-8
NN = [1, 1]
regs = [1, 2]
n_regs = 2
esp_R = [5, 5] """

N = 4
cce = 1
ccd = 0
prec = 10e-6
NN = [1, 1]
regs = [1, 2]
n_regs = 2
esp_R = [5, 5]

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

final_fi, psiX, iteracao, abs_rate, escape_rate, execution_time = med(
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
print(psiX)

print(50 * "-")

final_fi, psiX, iteracao, escape_rate, execution_time = response_matrix(
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

print(psiX)
