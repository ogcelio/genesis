# Simulador Nuclear
Projeto de IC do Instituto Politécnico da Universidade do Estado do Rio de Janeiro

## LEMBRAR:
- Trocar precisão por "Qtd. de Casas Decimais"
- CASO VÁ RODAR O SIMULADOR EM UM COMPUTADOR PESSOAL:
  
  1: Por segurança, crie um ambiente virtual rodando o seguinte comando no terminal:
  ```md
  python -m venv venv
  ```
  Obs.: O segundo venv representa o nome da pasta do ambiente virtual que, por convenção, é venv.

  2: IMPORTANTE: Habilite o ambiente virtual rodando o seguinte comando no terminal (Windows):
  ```md
  .\venv\Scripts\activate
  ```

  3: Instale todos os requerimentos para que o simulador seja executado com o seguinte comando:
  ```md
  pip install -r .\requirements.txt
  ```

  4: Certifique-se que o código está sendo interpretado com o python correto, o que pode ser conferido na parte de baixo do VS Code
  Exemplo: Python 3.13.1 ('venv':venv)

  5: Pronto, você pode rodar normalmente o simulador. Toda alteração ou instalação feita com o ambiente virtual ativado não afeta o computador de forma global. Para desativar, basta digitar no terminal:
  ```md
  deactivate
  ```
## Método Diamond Difference
<details>
  <summary>Método</summary>
  
  ```py
  import os
import sys

import numpy as np

# Tornando a quadratura possível de ser importada
path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura


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
    precisao,
    NN,
    regioes,
    n_regioes,
    esp_R,
):
    iteracao = 0  # Iniciando as iterações
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    pt = sum(NN) + 1  # Número de pontos totais
    NNT = sum(NN)  # Número de nodos totais

    teste_0 = False
    for i in range(len(Qj)):
        if Qj[i] != 0.0:
            teste_0 = True  # Teste para saber se todas as fontes são 0
            break

    hj = [0 for _ in range(n_regioes)]
    for regiao in range(n_regioes):
        hj[regiao] = esp_R[regiao] / NN[regiao]  # Espessura do nodo

    ###ETAPA estimativas iniciais:
    psiX = [[0 for _ in range(N)] for _ in range(pt)]  # criando lista com psis iniciais
    for i in range(N // 2):
        psiX[0][i] = cce
        psiX[NNT][N // 2 + i] = ccd

    while True:
        iteracao += 1
        ###ETAPA CÁLCULO DOS PSIS MÉDIOS
        psiM = []
        for j in range(NNT):
            psiM_aux = []
            for m in range(N):
                psiM_aux.append((1 / 2) * (psiX[j + 1][m] + psiX[j][m]))
            psiM.append(psiM_aux)

        ###ETAPA CÁLCULO DO Ssj
        regiao = regioes[0] - 1
        nodo = 0
        Ssj = []
        i = 0
        for j in range(NNT):
            soma = 0
            if nodo == NN[i]:
                i += 1
                regiao = regioes[i] - 1
                nodo = 0

            for m in range(N):
                soma += w[m] * psiM[j][m]
            Ssj.append((sigmaS0[regiao] / 2) * soma)
            nodo += 1

        ###ETAPA CÁLCULO DO FI INICIAL
        fi_inicial = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_inicial.append((1 / 2) * soma_fi)

        if ccd == 0.0 and cce == 0.0 and teste_0 == False:
            # Arredondando fi_final
            fi_inicial_formatado = [float(fi) for fi in fi_inicial]

            # Arredondando psiX
            psiX_formatado = [[float(f"{fluxo}") for fluxo in linha] for linha in psiX]
            taxa_absorcao = [0 for _ in range(n_regioes)]
            taxa_fuga = [0, 0]
            return (
                fi_inicial_formatado,
                psiX_formatado,
                iteracao,
                taxa_absorcao,
                taxa_fuga,
            )  # Caso fontes e condições de contorno sejam nulas, o código retorna os fluxos completamente preenchidos de zeros

        ###ETAPA IDA
        regiao = regioes[0] - 1
        nodo = 0
        i = 0
        for j in range(1, pt):
            if nodo == NN[i]:
                i += 1
                regiao = regioes[i] - 1
                nodo = 0
            for m in range(N // 2):
                psiX[j][m] = (
                    (((mi[m] / hj[i]) - (sigmaT[regiao] / 2)) * psiX[j - 1][m])
                    + Ssj[j - 1]
                    + Qj[regiao]
                ) / ((mi[m] / hj[i]) + (sigmaT[regiao] / 2))
            nodo += 1

        ###ETAPA VOLTA
        ultima_regiao = len(regioes) - 1
        regiao = regioes[ultima_regiao] - 1
        nodo = 0
        i = ultima_regiao
        for j in range(NNT - 1, -1, -1):
            if nodo == NN[i]:
                i -= 1
                regiao = regioes[i] - 1
                nodo = 0
            for m in range((N // 2), N):
                psiX[j][m] = (
                    (((abs(mi[m]) / hj[i]) - (sigmaT[regiao] / 2)) * psiX[j + 1][m])
                    + Ssj[j]
                    + Qj[regiao]
                ) / ((abs(mi[m]) / hj[i]) + (sigmaT[regiao] / 2))
            nodo += 1

        ###ETAPA CÁLCULO DO FI FINAL
        fi_final = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_final.append((1 / 2) * soma_fi)

        if iteracao > 1:
            ###ETAPA CÁLCULO DO DR

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
    fi_final_formatado = [round(float(fi), 4) for fi in fi_final]

    # Arredondando psiX
    psiX_formatado = [[float(f"{fluxo:.4f}") for fluxo in linha] for linha in psiX]

    # TAXA DE ABSORÇÃO
    fi_medio = []
    sigmaA = []
    soma = 0
    for j in range(NNT):
        for m in range(N):
            soma += w[m] * psiM[j][m]
        fi_medio.append((1 / 2) * soma)
        soma = 0

    # Gerando Sigma A
    for regiao in range(len(sigmaT)):
        sigmaA.append(sigmaT[regiao] - sigmaS0[regiao])

    regiao = regioes[0] - 1
    taxa_absorcao = []
    soma = 0
    nodo = 1
    i = 0
    for j in range(NNT):
        soma += sigmaA[regiao] * fi_medio[j] * hj[regiao]
        if nodo == NN[i]:
            i += 1
            if i < len(regioes):
                regiao = regioes[i] - 1
            taxa_absorcao.append(soma / esp_R[regiao])
            soma = 0
            nodo = 0
        nodo += 1

    # FUGA EM 0
    taxa_fuga = []
    soma = 0
    for m in range(N // 2, N):
        soma += abs(mi[m] * w[m] * psiX[0][m])
    taxa_fuga.append(soma)

    # FUGA NO MÁXIMO DA ÚLTIMA REGIÃO
    soma = 0
    for m in range(N // 2):
        soma += abs(mi[m] * w[m] * psiX[len(psiX) - 1][m])
    taxa_fuga.append(soma)

    return fi_final_formatado, psiX_formatado, iteracao, taxa_absorcao, taxa_fuga
  ```

</details>

## Método MED
<details>
  <summary>Método</summary>
  
  ```py
import os
import sys
import numpy as np

path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura


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
    precisao,
    NN,
    regioes,
    n_regioes,
    esp_R,
):
    ###ETAPA INICIALIZANDO VARIÁVEIS
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    pt = sum(NN) + 1  # Número de pontos totais
    NNT = sum(NN)  # Número de nodos totais

    teste_0 = False
    for i in range(len(Qj)):
        if Qj[i] != 0.0:
            teste_0 = True  # Teste para saber se todas as fontes são 0
            break

    psiX = [[0 for _ in range(N)] for _ in range(pt)]  # Criando lista com psis iniciais
    for i in range(N // 2):
        psiX[0][i] = cce
        psiX[NNT][N // 2 + i] = ccd

    hj = [0 for _ in range(n_regioes)]
    for regiao in range(n_regioes):
        hj[regiao] = esp_R[regiao] / NN[regiao]  # Espessura do nodo

    C0j = []
    for i in range(len(sigmaT)):
        C0j.append(sigmaS0[i] / sigmaT[i])

    iteracao = 0
    while True:
        psiM = [[0 for _ in range(N)] for _ in range(NNT)]
        iteracao += 1
        ###ETAPA CÁLCULO DO FI INICIAL
        fi_inicial = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_inicial.append((1 / 2) * soma_fi)

        if ccd == 0.0 and cce == 0.0 and teste_0 == False:
            # Arredondando fi_final
            fi_inicial_formatado = [float(fi) for fi in fi_inicial]

            # Arredondando psiX
            psiX_formatado = [[float(f"{fluxo}") for fluxo in linha] for linha in psiX]
            taxa_absorcao = [0 for _ in range(n_regioes)]
            taxa_fuga = [0, 0]
            return (
                fi_inicial_formatado,
                psiX_formatado,
                iteracao,
                taxa_absorcao,
                taxa_fuga,
            )  # Caso fontes e condições de contorno sejam nulas, o código retorna os fluxos completamente preenchidos de zeros

        # REALIZANDO O MESMO PROCESSO PARA CADA NODO
        regiao = regioes[0] - 1
        contador = 0
        k = 0
        for nodo in range(NNT):
            if contador == NN[k]:
                k += 1
                regiao = regioes[k] - 1
                contador = 0

            matriz_A = [[0 for _ in range(N)] for _ in range(N)]
            matriz_P = [[0 for _ in range(N)] for _ in range(N)]

            ###ETAPA CÁLCULO DA MATRIZ DE AUTOVALORES E AUTOVETORES
            for i in range(N):
                for j in range(N):
                    if i == j:
                        matriz_A[i][j] = float(
                            (1 / mi[i]) - ((C0j[regiao] * w[j]) / (2 * mi[i]))
                        )
                    else:
                        matriz_A[i][j] = float(-((C0j[regiao] * w[j]) / (2 * mi[i])))

            # ENCONTRANDO AUTOVALORES E AUTOVETORES
            autovalor_lambda, autovetor = np.linalg.eig(matriz_A)
            autovalores = autovalor_lambda.tolist()
            autovetores = autovetor.tolist()

            # TRANSFORMANDO LAMBDA EM NI
            for i, autovalor in enumerate(autovalores):
                autovalores[i] = 1 / autovalor

            ###ETAPA CÁLCULO DA MATRIZ DA SOLUÇÃO PARTICULAR
            for i in range(N):
                for j in range(N):
                    if i == j:
                        matriz_P[i][j] = float(
                            sigmaT[regiao] - ((sigmaS0[regiao] * w[j]) / 2)
                        )
                    else:
                        matriz_P[i][j] = float(-((sigmaS0[regiao] * w[j]) / 2))
            matriz_P_inv = np.linalg.inv(matriz_P)

            fonte = [float(Qj[regiao]) for _ in range(N)]
            solucao_particular = (matriz_P_inv @ fonte).tolist()

            ###ETAPA CÁLCULO DO VETOR SOLUÇÃO PARA OS ALFAS
            vetor_solucao = [0 for _ in range(N)]
            for i in range(N // 2):
                vetor_solucao[i] = float(psiX[nodo][i]) - solucao_particular[i]
                vetor_solucao[N // 2 + i] = (
                    float(psiX[nodo + 1][N // 2 + i]) - solucao_particular[N // 2 + i]
                )

            # CÁLCULO DA MATRIZ GERADORA DOS ALFAS
            matriz_alfa = [[0 for _ in range(N)] for _ in range(N)]

            for i in range(N // 2):
                # PARTE DE CIMA DA MATRIZ
                for j in range(N):
                    if autovalores[j] > 0:
                        exponencial = 1
                    else:
                        exponencial = np.exp(
                            float(-sigmaT[regiao] * hj[regiao]) / abs(autovalores[j])
                        )

                    matriz_alfa[i][j] = autovetores[i][j] * exponencial

                # PARTE DE BAIXO DA MATRIZ
                for i in range(N // 2, N):
                    for j in range(N):
                        if autovalores[j] < 0:
                            exponencial = 1
                        else:
                            exponencial = np.exp(
                                float(-sigmaT[regiao] * hj[regiao])
                                / abs(autovalores[j])
                            )

                        matriz_alfa[i][j] = autovetores[i][j] * exponencial

            matriz_alfa_inv = np.linalg.inv(matriz_alfa)

            # CÁLCULO DOS ALFAS
            alfa = matriz_alfa_inv @ vetor_solucao

            ###ETAPA ATUALIZANDO PSIS
            for i in range(N // 2):
                soma = 0
                for j in range(N):
                    if autovalores[j] < 0:
                        exponencial = 1
                    else:
                        exponencial = np.exp(
                            float(-sigmaT[regiao] * hj[regiao]) / abs(autovalores[j])
                        )

                    soma += alfa[j] * autovetores[i][j] * exponencial

                psiX[nodo + 1][i] = soma + solucao_particular[i]

            for i in range(N // 2, N):
                soma = 0
                for j in range(N):
                    if autovalores[j] > 0:
                        exponencial = 1
                    else:
                        exponencial = np.exp(
                            float(-sigmaT[regiao] * hj[regiao]) / abs(autovalores[j])
                        )
                    soma += alfa[j] * autovetores[i][j] * exponencial

                psiX[nodo][i] = soma + solucao_particular[i]

            ###ETAPA ATUALIZANDO PSIS MÉDIOS
            for i in range(N):
                soma = 0
                for j in range(N):
                    if autovalores[j] > 0:
                        exponencial = 1 - np.exp(
                            float(-sigmaT[regiao] * hj[regiao]) / abs(autovalores[j])
                        )
                    else:
                        exponencial = (
                            np.exp(
                                float(-sigmaT[regiao] * hj[regiao])
                                / abs(autovalores[j])
                            )
                            - 1
                        )

                    soma += autovalores[j] * alfa[j] * autovetores[i][j] * exponencial
                psiM[nodo][i] = (
                    float(1 / (hj[regiao] * sigmaT[regiao])) * soma
                ) + solucao_particular[i]

            ###ETAPA CÁLCULO DO FI FINAL
            fi_final = []
            for x in range(pt):
                soma_fi = 0
                for m in range(N):
                    soma_fi += w[m] * psiX[x][m]
                fi_final.append((1 / 2) * soma_fi)

            contador += 1

        if iteracao == 1 and n_regioes == 1 and NNT == 1:
            fi_final = np.array(fi_final)
            break
        elif iteracao > 1:
            ###ETAPA CÁLCULO DO DR

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
    fi_final_formatado = [round(float(fi), 6) for fi in fi_final]

    # Arredondando psiX
    psiX_formatado = [[float(f"{fluxo:.6f}") for fluxo in linha] for linha in psiX]

    ###ETAPA TAXA DE ABSORÇÃO
    fi_medio = []
    sigmaA = []
    soma = 0
    for j in range(NNT):
        for m in range(N):
            soma += w[m] * psiM[j][m]
        fi_medio.append((1 / 2) * soma)
        soma = 0

    # Gerando Sigma A
    for regiao in range(len(sigmaT)):
        sigmaA.append(sigmaT[regiao] - sigmaS0[regiao])

    regiao = regioes[0] - 1
    taxa_absorcao = []
    soma = 0
    nodo = 1
    i = 0
    for j in range(NNT):
        soma += sigmaA[regiao] * fi_medio[j] * hj[regiao]
        if nodo == NN[i]:
            i += 1
            if i < len(regioes):
                regiao = regioes[i] - 1
            taxa_absorcao.append(soma / esp_R[regiao])
            soma = 0
            nodo = 0
        nodo += 1

    ##ETAPA TAXA DE FUGA
    # FUGA EM 0
    taxa_fuga = []
    soma = 0
    for m in range(N // 2, N):
        soma += abs(mi[m] * w[m] * psiX[0][m])
    taxa_fuga.append(soma)

    # FUGA NO MÁXIMO DA ÚLTIMA REGIÃO
    soma = 0
    for m in range(N // 2):
        soma += abs(mi[m] * w[m] * psiX[len(psiX) - 1][m])
    taxa_fuga.append(soma)

    return fi_final_formatado, psiX_formatado, iteracao, taxa_absorcao, taxa_fuga
  ```
</details>
