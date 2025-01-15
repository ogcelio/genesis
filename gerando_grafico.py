import os  # biblioteca de sistema operacional

import matplotlib.pyplot as plt  # biblioteca para plotagem
import numpy as np  # biblioteca para operações matemáticas
from matplotlib.colors import Normalize, to_hex  # coleta de cores e normalização

from metodo_dd_simples_final import diamond_difference  # importando o dd


# Gerando o gráfico principal
def gerar_tela(Z, NN, esp_Z, fi_final):
    # Gerando lista com todos* os pontos do domínio
    dominio = []
    hj = esp_Z / NN
    for i in range(NN + 1):
        dominio.append(i * hj)

    esp_T = esp_Z * Z  # Espessura total

    plt.figure(figsize=(5.5, 5.2))  # NÃO MUDE; Definindo tamanho da figura
    # fig.subplots_adjust(left=0.2, right=0.85, top=0.85, bottom=0.2)  # NÃO APAGUE
    plt.xlim(
        0, (esp_Z * Z)
    )  # Definindo até onde o gráfico vai em x (último ponto do domínio)
    plt.grid(True)  # Ativando linhas do gráfico

    if esp_T > 25:
        escala = 5
    else:
        escala = esp_T / esp_Z
    plt.xticks(np.arange(0, esp_T + hj, escala))  # Definindo a escala do domínio

    # Plotando o gráfico de linhas
    plt.plot(dominio, fi_final, color="lime", zorder=2, label="Diamond Difference")
    # Plotando pontos dos fluxos escalares
    plt.scatter(
        dominio,
        fi_final,
        s=100,
        color="darkslategray",
        edgecolor="black",
        linewidth=1,
        zorder=1,
    )

    # Definindo legendas para os eixos
    plt.xlabel("Domínio (cm)", fontsize=10)
    plt.ylabel("Fluxo escalar médio (Nêutrons/cm$^2$s)", fontsize=10)

    # Definindo o endereço para o salvamento do arquivo
    base_path = os.path.abspath(os.getcwd())

    # Certificando de que o diretório existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # Caso não exista, o diretório é criado

    # Juntando o caminho do arquivo com o seu nome
    save_path = os.path.join(base_path, "Grafico.png")

    # Criando legenda e definindo a sua localização (melhor possível)
    plt.legend(loc="best")

    # Salvando a figura
    plt.savefig(save_path, dpi=80, bbox_inches="tight")

    plt.close()  # Fechando a figura, já que aberta ela pode consumir muita memória

    return save_path, dominio  # Retorna o caminho de salvamento e o domínio


# Gerando o gráfico de intensidade
def intensidade(fi_final):
    # Coletando o fi máximo e o fi mínimo
    valor_maximo = max(fi_final)
    valor_minimo = min(fi_final)

    # Normalizar os dados para o intervalo [0, 1]
    norm = Normalize(vmin=valor_minimo, vmax=valor_maximo)
    plt.figure(figsize=(10, 0.8))  # Definindo o tamanho da figura

    # Definindo função para coletar as cores do gráfico, baseadas em um tema
    cmap = plt.get_cmap("YlOrRd")

    # Normalizando os valores para a faixa [0, 1]
    maximo_normalizado = norm(valor_maximo)
    minimo_normalizado = norm(valor_minimo)

    # Obtendo a cor correspondente
    cor_maximo = cmap(maximo_normalizado)
    cor_minimo = cmap(minimo_normalizado)

    # Convertendo a cor para formato hexadecimal
    max_hex = to_hex(cor_maximo)
    min_hex = to_hex(cor_minimo)

    gradient = np.array(fi_final).reshape(1, -1)  # Definindo o gradiente normalizado
    plt.imshow(gradient, aspect="auto", cmap="YlOrRd")  # Plotando o gráfico
    plt.axis("off")  # Desativando marcações de eixo

    # Definindo o endereço para o salvamento do arquivo
    base_path = os.path.abspath(os.getcwd())

    # Certificando de que o diretório existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # Caso não exista, o diretório é criado

    # Juntando o caminho do arquivo com o seu nome
    save_path = os.path.join(base_path, "intensidade.png")

    # Salvando a figura
    plt.savefig(save_path, dpi=50, bbox_inches="tight")

    plt.close()  # Fechando a figura, já que aberta ela pode consumir muita memória

    # Retorna onde é salvo, cor do máximo e cor do mínimo
    return save_path, max_hex, min_hex
