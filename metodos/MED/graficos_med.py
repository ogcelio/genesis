import os  # biblioteca de sistema operacional

import matplotlib.pyplot as plt  # biblioteca para plotagem
import numpy as np  # biblioteca para operações matemáticas
from matplotlib.colors import Normalize, to_hex  # coleta de cores e normalização
from PIL import Image, ImageDraw


# Gerando o gráfico principal
def gerar_tela_med(NN, esp_R, fi_final, regioes, n_regioes, abrir):
    # Gerando lista com todos* os pontos do domínio
    NNT = int(sum(NN))
    n_regioes = int(n_regioes)
    dominio = []
    hj = [0 for _ in range(n_regioes)]
    for regiao in range(n_regioes):
        hj[regiao] = esp_R[regiao] / NN[regiao]  # Espessura do nodo

    regiao = 0
    contador = 0
    espessura_atual = 0
    espessura_regiao = 0
    dominio.append(0.0)
    for i in range(NNT):
        if espessura_regiao == esp_R[contador]:
            espessura_regiao = 0
            contador += 1
            regiao = regioes[contador] - 1

        espessura_atual += hj[contador]
        espessura_regiao += hj[contador]
        dominio.append(espessura_atual)

    esp_T = sum(esp_R)  # Espessura total

    plt.figure(figsize=(5.55, 5.35))  # NÃO MUDE; Definindo tamanho da figura
    # fig.subplots_adjust(left=0.2, right=0.85, top=0.85, bottom=0.2)  # NÃO APAGUE
    plt.xlim(
        0, (esp_T)
    )  # Definindo até onde o gráfico vai em x (último ponto do domínio)
    plt.grid(True)  # Ativando linhas do gráfico

    escala = float(esp_T / 5)
    plt.xticks(
        np.arange(0, float(esp_T + 10e-10), escala)
    )  # Definindo a escala do domínio

    # Plotando o gráfico de linhas
    plt.plot(dominio, fi_final, color="cyan", zorder=2, label="MED")
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

    # Criando legenda e definindo a sua localização (melhor possível)
    plt.legend(loc="best")

    if abrir == True:
        plt.show()
        return

    # Definindo o endereço para o salvamento do arquivo
    base_path = os.path.abspath(os.getcwd())
    base_path = os.path.join(base_path, "imagens")

    # Certificando de que o diretório existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # Caso não exista, o diretório é criado

    # Juntando o caminho do arquivo com o seu nome
    save_path = os.path.join(base_path, "Grafico.png")

    # Salvando a figura
    plt.savefig(save_path, dpi=80, bbox_inches="tight", pad_inches=0.05)

    plt.close()  # Fechando a figura, já que aberta ela pode consumir muita memória

    return save_path, dominio  # Retorna o caminho de salvamento e o domínio


# Gerando o gráfico de intensidade
def intensidade(fi_final):
    # Coletando o fi máximo e o fi mínimo
    valor_maximo = float(max(fi_final))
    valor_minimo = float(min(fi_final))

    # Normalizar os dados para o intervalo [0, 1]
    norm = Normalize(vmin=valor_minimo, vmax=valor_maximo)
    plt.figure(figsize=(10.8, 1))  # Definindo o tamanho da figura

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
    base_path = os.path.join(base_path, "imagens")

    # Certificando de que o diretório existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # Caso não exista, o diretório é criado

    # Juntando o caminho do arquivo com o seu nome
    save_path = os.path.join(base_path, "intensidade.png")

    # Salvando a figura
    plt.savefig(save_path, dpi=50, bbox_inches="tight", pad_inches=0)

    plt.close()  # Fechando a figura, já que aberta ela pode consumir muita memória

    # Retorna onde é salvo, cor do máximo e cor do mínimo
    return save_path, max_hex, min_hex


def grafico_regioes(esp_R):
    esp_T = sum(esp_R)
    # Configurações da imagem
    largura = 509  # Largura da imagem
    altura = 19  # Altura da imagem
    cor_fundo = (20, 20, 184)  # Cor de fundo (RGB)
    cor_divisoria = (245, 245, 245)  # Cor das divisórias (RGB)

    # Lista de porcentagens para divisórias
    porcentagem_regiao = []
    for espessura in esp_R:
        porcentagem_regiao.append(espessura / esp_T)

    posicoes_divisorias = []
    i = 0
    for multiplicador in porcentagem_regiao:  # Posições X das divisórias
        if i == 0:
            posicoes_divisorias.append(multiplicador * largura)
        else:
            posicoes_divisorias.append(
                multiplicador * largura + posicoes_divisorias[i - 1]
            )
        i += 1

    # Criar imagem com fundo colorido
    imagem = Image.new("RGB", (largura, altura), cor_fundo)
    draw = ImageDraw.Draw(imagem)

    # Desenhar divisórias nas posições especificadas
    for x in posicoes_divisorias:
        draw.line([(x, 0), (x, altura)], fill=cor_divisoria, width=2)  # Linha vertical

    base_path = os.path.abspath(os.getcwd())
    base_path = os.path.join(base_path, "imagens")

    # Certificando de que o diretório existe
    if not os.path.exists(base_path):
        os.makedirs(base_path)  # Caso não exista, o diretório é criado

    # Juntando o caminho do arquivo com o seu nome
    save_path = os.path.join(base_path, "grafico_regioes.png")

    # Salvar ou exibir a imagem
    imagem.save(save_path)

    return save_path
