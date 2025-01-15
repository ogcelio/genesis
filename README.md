# Simulador_Nuclear
Projeto de IC do Instituto Politécnico da Universidade do Estado do Rio de Janeiro

## LEMBRAR:
- Fazer a proteção "anti-erros" no código do simulador

## Método Diamond Difference
<details>
  <summary>Método</summary>
  
  ```py
  import numpy as np

from quadratura_backend import quadratura


def diamond_difference(N, NN, Z, esp_Z, sigmaT, sigmaS0, Qj, precisao, cce, ccd):
    iteracao = 0  # Iniciando as iterações
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    pt = NN + 1  # Número de pontos totais
    hj = esp_Z / NN  # Espessura do nodo
    Qj = Qj / NN
    ###ETAPA estimativas iniciais:  CORRETO
    psiX = [[0 for _ in range(N)] for _ in range(pt)]  # criando lista com psis iniciais
    for i in range(N // 2):
        psiX[0][i] = cce
        psiX[NN][i + 2] = ccd

    while True:
        iteracao += 1  #  Contagem de Iterações

        ###ETAPA CÁLCULO DOS PSIS MÉDIOS    CORRETO
        psiM = []
        for j in range(NN):
            psiM_aux = []
            for m in range(N):
                psiM_aux.append((1 / 2) * (psiX[j + 1][m] + psiX[j][m]))
            psiM.append(psiM_aux)

        ###ETAPA CÁLCULO DO Ssj    CORRETO
        Ssj = []
        for j in range(NN):
            soma = 0
            for m in range(N):
                soma += w[m] * psiM[j][m]
            Ssj.append((sigmaS0 / 2) * soma)

        ###ETAPA CÁLCULO DO FI INICIAL    CORRETO
        fi_inicial = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_inicial.append((1 / 2) * soma_fi)

        ###ETAPA IDA    CORRETO
        for j in range(1, pt):
            for m in range(N // 2):
                psiIDA_novo = (
                    (((mi[m] / hj) - (sigmaT / 2)) * psiX[j - 1][m]) + Ssj[j - 1] + Qj
                ) / ((mi[m] / hj) + (sigmaT / 2))
                psiX[j][m] = psiIDA_novo

        ###ETAPA VOLTA    CORRETO
        for j in range(NN - 1, -1, -1):
            for m in range((N // 2), N):
                psiVOLTA_novo = (
                    (((abs(mi[m]) / hj) - (sigmaT / 2)) * psiX[j + 1][m]) + Ssj[j] + Qj
                ) / ((abs(mi[m]) / hj) + (sigmaT / 2))
                psiX[j][m] = psiVOLTA_novo

        ###ETAPA CÁLCULO DO FI FINAL    CORRETO
        fi_final = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_final.append((1 / 2) * soma_fi)

        if iteracao > 1:
            ###ETAPA CÁLCULO DO DR   CORRETO

            # Transformando em arrays numpy para realizar a subtração
            fi_inicial = np.array(fi_inicial)
            fi_final = np.array(fi_final)

            resultado = abs(fi_inicial - fi_final)

            # Transformando em listas
            resultado = resultado.tolist()
            fi_inicial = fi_inicial.tolist()

            # Coletando os maiores de cada vetor, em módulo
            maior_inicial = max(fi_inicial, key=abs)
            maior_final = max(resultado, key=abs)

            dr = abs(maior_final / maior_inicial)
            if dr < precisao:
                break

    # Arredondando fi_final
    fi_final = fi_final.tolist()
    fi_final_formatado = [round(num, 4) for num in fi_final]

    # Como psiX é uma matriz, deve ser arredondado com auxílio da Numpy
    psiX_formatado = np.array(psiX).round(4)
    psiX_formatado = psiX_formatado.tolist()

    return fi_final_formatado, psiX_formatado, iteracao
  ```

</details>
