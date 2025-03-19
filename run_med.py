import json
import os
import sys
from decimal import Decimal, getcontext
from metodos.MED.med_revisado import med

getcontext().prec = 50

path = "dados\\propriedades.json"
with open(path, "r", encoding="utf8") as file:
    propriedades_1grupo = json.load(file)

# PROPRIEDADES MATERIAIS 1G

sigmaT = propriedades_1grupo["sigmaT"]
sigmaS0 = propriedades_1grupo["sigmaS0"]
sigmaS1 = propriedades_1grupo["sigmaS1"]
sigmaS2 = propriedades_1grupo["sigmaS2"]
Qj = propriedades_1grupo["Qj"]
NiSigmaF = propriedades_1grupo["NiSigmaF"]

for i in range(len(sigmaT)):
    sigmaT[i] = Decimal(sigmaT[i])
    sigmaS0[i] = Decimal(sigmaS0[i])
    sigmaS1[i] = Decimal(sigmaS1[i])
    sigmaS2[i] = Decimal(sigmaS2[i])
    Qj[i] = Decimal(Qj[i])
    NiSigmaF[i] = Decimal(NiSigmaF[i])

med(
    sigmaT,
    sigmaS0,
    sigmaS1,
    sigmaS2,
    Qj,
    NiSigmaF,
    N=Decimal("4"),
    cce=Decimal("1"),
    ccd=Decimal("0"),
    precisao=10e-6,
    NN=[Decimal("1")],
    regioes=[1],
    n_regioes=Decimal("1"),
    esp_R=[Decimal("5")],
)
# print(ni, "\n\n", am, "\n\n", solucoes)
