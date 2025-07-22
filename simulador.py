# OBJETIVOS:
# MELHORAR A EFICIÊNCIA DO CÓDIGO;
# MUDAR A APARÊNCIA DA INTERFACE DO SIMULADOR; CORRETO
# TORNAR A FUNÇÃO SEM ERROS NUMA FUNÇÃO "GLOBAL", QUE VERIFICA OS ERROS E RETORNA O ERRO ESPECÍFICO PRESENTE NO ARQUIVO "ERROS"; CORRETO
# ADICIONAR AS FUNÇÕES MULTIGRUPO;
# ADICIONAR UMA FUNÇÃO EM QUE PERMITA MESCLAR DOIS GRÁFICOS DE DOIS MÉTODOS DIFERENTES, PARA QUE ELES SEJAM COMPARADOS; CORRETO
# ADICIONAR UMA JANELA DE "PREFERÊNCIAS" NO SIMULADOR, EM QUE NELA ACONTECERÁ:
#   1- ESCOLHA ENTRE TEMA CLARO E ESCURO;
#   2- CONFIGURAÇÕES DO SIMULADOR;
#   3- MAIS OPÇÕES.
# ADICIONAR NOVOS MÉTODOS:
#   1- MED MODIFICADO; CORRETO
#   2- SPECTRAL GREEN'S FUNCTION (SGF).

import platform
import sys
import json
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette, QColor, QFont, QFontDatabase

from PySide6.QtWidgets import (
    QMainWindow,
    QDialog,
    QApplication,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QMessageBox,
    QTableWidgetItem,
)

from dashboards.dashboard_simulador import (
    Ui_MainWindow,  # Importando a dashboard do simulador
)
from dashboards.janela_propriedades import (
    propriedades,
)  # Importando tela de propriedades
from dashboards.janela_resultados_1G import (
    Ui_resultados_1G,  # Importando a tela de resultados 1G
)

# Importando janela de ajuda
from dashboards.janela_ajuda import Janela_Instrucoes

# Importando janela de taxas
from dashboards.janela_taxas import Ui_taxas_resultado

from metodos.dd_main import (
    diamond_difference,  # Importando o Diamond Difference
)
from metodos.med_main import med  # Importando o MED
from metodos.med_mod_main import med_mod
from metodos.common.graphics import (
    main_graphic,
    heat_graphic,
    reg_graphic,
    combo_chart,
)  # Geradores das imagens
from metodos.common.init_variables import init_hj
from mensagens.erros import *

# Criação de variáveis que serão mostradas
fi_final, dominio, psiX, taxa_absorcao, taxa_fuga, regioes, NN = ([] for _ in range(7))

if platform.system() == "Windows":
    props_path = "dados\\reatores.json"
    relatorio_path = "dados\\relatorio.txt"
    cache_path = "dados\\cache.json"
    reator_path = "dados\\cache_reator.txt"
    fonte_path = "fontes\\Roboto-VariableFont_wdth,wght.ttf"
    path_logo_iprj = "imagens\\logo_iprj_white.png"
    path_logo_labtran = "imagens\\logo_labtran_white.png"
    path_logo_coppe = "imagens\\logo_coppe_white.png"
    path_logo_simulador = "imagens\\genesis.png"
else:
    props_path = "dados/reatores.json"
    relatorio_path = "dados/relatorio.txt"
    cache_path = "dados/cache.json"
    reator_path = "dados/cache_reator.txt"
    fonte_path = "fontes/Roboto-VariableFont_wdth,wght.ttf"
    path_logo_iprj = "imagens/logo_iprj_white.png"
    path_logo_labtran = "imagens/logo_labtran_white.png"
    path_logo_coppe = "imagens/logo_coppe_white.png"
    path_logo_simulador = "imagens/genesis.png"

with open(relatorio_path, "w") as file:
    pass
with open(cache_path, "w") as file:
    json.dump({}, file, indent=2)
esp_R = 0
n_regioes = 0
method = ""
primeiro_calculo = False
ordem_metodo = 0
duracao = 0
iteracao = 0
propriedades_1grupo = {}
reator = ""
metodo = ""


class dashboard_simulador(QMainWindow):
    def __init__(self, *args, **argvs):
        super(dashboard_simulador, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        # Define o estilo Fusion para mudar a paleta
        app.setStyle("Fusion")

        # Definindo fonte
        id_fonte = QFontDatabase.addApplicationFont(fonte_path)
        font_families = QFontDatabase.applicationFontFamilies(id_fonte)
        if font_families:
            fonte = font_families[0]
            fonte_qt = QFont(fonte, 12)
        app.setFont(fonte_qt)

        # Criar uma paleta clara
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
        palette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
        palette.setColor(QPalette.ToolTipText, Qt.black)
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(0, 122, 204))
        palette.setColor(QPalette.Highlight, QColor(0, 122, 204))
        palette.setColor(QPalette.HighlightedText, QColor(240, 240, 240))
        app.setPalette(palette)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_window()  # Centraliza a dashboard
        self.ui.etapa.setReadOnly(
            True
        )  # Impede que a caixa de texto de "etapa" seja editada pelo usuário

        # ----------------------COLOCANDO LOGOS----------------------
        # PRIMEIRA --------------------------------------------------
        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(path_logo_iprj)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.logo_1.setScene(cena_grafico)

        # SEGUNDA ---------------------------------------------------
        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(path_logo_labtran)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.logo_2.setScene(cena_grafico)

        # TERCEIRA --------------------------------------------------
        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(path_logo_coppe)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.logo_3.setScene(cena_grafico)

        # NOME SIMULADOR --------------------------------------------------
        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(path_logo_simulador)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.nome_simulador.setScene(cena_grafico)
        # -----------------------------------------------------------
        self.ui.ok_regioes.clicked.connect(self.regioes)  # Edita número de regiões
        self.ui.actionRelatorio.triggered.connect(self.mostrar_relatorio)
        self.ui.actionDiamond_Difference_DD.triggered.connect(
            lambda: self.iniciar_calculo(method="Diamond Difference")
        )  # Inicia o processo de cálculo do DD
        self.ui.actionMED.triggered.connect(
            lambda: self.iniciar_calculo(method="SDM")
        )  # Inicia o processo de cálculo do MED
        self.ui.actionMED_Modificado.triggered.connect(
            lambda: self.iniciar_calculo(method="MSD")
        )  # Inicia o processo de cálculo do MED Modificado
        self.ui.actionFisicos_Materiais_1G.triggered.connect(
            self.abrir_propriedades_1G
        )  # Abre as propriedades 1G
        self.ui.actionNumericos_1G.triggered.connect(
            self.abrir_resultados_1G
        )  # Abre os resultados 1G
        self.ui.actionSair.triggered.connect(
            self.close
        )  # Fecha a janela ao clicar em sair
        # Limpa o histórico
        self.ui.actionLimpar.triggered.connect(self.limpar)
        self.ui.actionMostrarGraficos.triggered.connect(self.mostrar_graficos)
        self.ui.actionMesclarMetodos.triggered.connect(self.mesclar_graficos)
        self.ui.actionAjuda.triggered.connect(
            self.abrir_ajuda
        )  # Abre a janela de ajuda

    def carregar_propriedades(self):
        global propriedades_1grupo, reator
        try:
            with open(props_path, "r", encoding="utf8") as file:
                reatores_1grupo = json.load(file)

            with open(reator_path, "r", encoding="utf8") as file:
                reator = file.read()

            propriedades_1grupo = reatores_1grupo[reator]
        except FileNotFoundError:
            raise reator_nao_selecionado

    def center_window(self):
        # Pega o retângulo da tela principal
        ret_tela = QApplication.primaryScreen().availableGeometry()

        # Pega o tamanho da janela atual
        ret_janela = self.frameGeometry()

        # Centraliza a posição da janela na tela
        centro = ret_tela.center()
        ret_janela.moveCenter(centro)

        # Ajusta a posição da janela
        self.move(ret_janela.topLeft())

    # Limpa o relatório e o cache
    def limpar(self):
        with open(relatorio_path, "w") as file:
            pass
        with open(cache_path, "w") as file:
            json.dump({}, file, indent=2)

    def mostrar_relatorio(self):
        global relatorio_path
        if platform.system() == "Windows":
            os.system(relatorio_path)
        else:
            os.system(f"open {relatorio_path}")

    def iniciar_calculo(self, method):
        global esp_R, duracao, iteracao, fi_final, psiX, taxa_absorcao, taxa_fuga, N, sigmaT, sigmaS0, Qj, cce, ccd, precisao, n_regioes, regioes, NN, ordem_metodo, reator
        # Espessuras globais para que sejam utilizadas posteriormente

        # Atualizando etapa
        self.ui.etapa.setText("CALCULANDO")
        QApplication.processEvents()  # Atualiza a tela

        sem_erros = self.iniciar_metodo(metodo_func=method)
        if (
            sem_erros != True
        ):  # Se sem_erros for diferente de True, o método não finaliza
            return

        self.ui.etapa.setText("GERANDO GRÁFICOS")
        QApplication.processEvents()  # Atualiza a tela

        *_, esp_R = self.coletar_dados()  # Coletando número de regiões e espessura
        soma = sum(esp_R)  # Fazendo a soma de todas as espessuras

        self.ui.espessura_total.setText(
            f"{soma}"
        )  # Colocando a espessura total na label

        # GRÁFICO -----------------------------------

        # Coleta o domínio e o caminho de salvamento do gráfico do DD
        save_path_grafico = reg_graphic(esp_R)

        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(save_path_grafico)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.grafico_espessura.setScene(cena_grafico)
        # ---------------------------
        # Atualizando etapa
        self.ui.etapa.setText("FINALIZADO")
        QApplication.processEvents()  # Atualiza a tela

        with open(cache_path, "r", encoding="utf8") as file:
            resultados = json.load(file)

        hj = init_hj(NN, n_regioes, esp_R)
        resultados.update(
            [
                (
                    f"{ordem_metodo}",
                    {
                        "metodo": method,
                        "fi_final": fi_final.tolist(),
                        "hj": hj.tolist(),
                        "NN": NN,
                    },
                )
            ]
        )
        with open(cache_path, "w+", encoding="utf8") as file:
            json.dump(resultados, file, indent=2)

        with open(relatorio_path, "+a", encoding="utf8") as file:
            file.write(
                f"Método Executado: {method}\n"
                f"Tempo de Execução: {duracao:.6f} segundos\n"
                f"Número de Iterações: {iteracao}\n\n"
                "PROPRIEDADES:\n\n"
                f"Ordem da Quadratura: {N}\n"
                f"Condição de Contorno Esquerda: {cce}\n"
                f"Condição de Contorno Direita: {ccd}\n"
                f"Precisão: {precisao}\n"
                f"Número de Regiões: {n_regioes}\n"
                f"CONJUNTO DE PROPRIEDADES: {reator}\n"
                f"Zonas Materiais: {regioes}\n"
                f"Número de Nodos por Região: {NN}\n"
                f"Espessura por Região (cm): {esp_R}\n"
                f"Fonte Fixa: {[fonte for fonte in Qj[0:n_regioes]]}\n\n"
                "Sigma T:\n"
                f"{[sigma for sigma in sigmaT[0:n_regioes]]}\n\n"
                "Sigma S0:\n"
                f"{[sigma for sigma in sigmaS0[0:n_regioes]]}\n\n"
                "RESULTADOS:\n\n"
                "Fluxos Escalares:\n"
                f"{fi_final}\n\n"
                "Fluxos Angulares:\n"
                f"{psiX}\n\n"
                "Taxa de Absorção:\n"
                f"{taxa_absorcao}\n\n"
                "Taxa de Fuga:\n"
                f"{taxa_fuga}"
                f"\n\n\n{50*"-"}\n\n\n"
            )
        self.abrir_resultados_1G()
        ordem_metodo += 1

    def iniciar_metodo(self, metodo_func):
        # As variáveis precisam ser globais para que sejam utilizadas em outras funções
        global psiX, fi_final, dominio, taxa_absorcao, taxa_fuga, n_regioes, regioes, NN, primeiro_calculo, method, duracao, iteracao, N, sigmaT, sigmaS0, Qj, cce, ccd, precisao, esp_R, duracao, metodo, iteracao
        metodo = metodo_func
        try:
            (
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
            ) = self.coletar_dados()  # Coleta os dados necessários

            detectar_erros(sigmaT, N, NN, regioes, esp_R)
        except ValueError:
            # Atualizando etapa
            self.ui.etapa.setText("ERRO VI-001")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-001: VALOR INVÁLIDO",
                "Certifique-se de que você digitou todos os dados corretamente, sem caixas em branco.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False  # Retorna False se algum erro ocorrer
        except quadratura_invalida:
            self.ui.etapa.setText("ERRO VI-002")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-002: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor par, inteiro e maior que zero para a ordem da quadratura.",
            )
            return False
        except nodo_invalido:
            self.ui.etapa.setText("ERRO VI-003")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-003: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor inteiro e maior que zero para o número de nodos de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except espessura_zero:
            self.ui.etapa.setText("ERRO VI-004")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-004: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor maior que zero para a espessura de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except regiao_invalida:
            self.ui.etapa.setText("ERRO VI-005")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-005: VALOR INVÁLIDO",
                f"Certifique-se de que você escolheu um valor inteiro para a zona entre 1 e {len(sigmaT)}.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except reator_nao_selecionado:
            self.ui.etapa.setText("ERRO AI-003")
            QMessageBox.information(
                QMessageBox(),
                "ERRO AI-003: AÇÃO INVÁLIDA",
                f"Certifique-se de que você escolheu um conjunto de propriedades na tela de propriedades antes de rodar o método.",
            )
            return False
        if metodo_func == "Diamond Difference":
            fi_final, psiX, iteracao, taxa_absorcao, taxa_fuga, duracao = (
                diamond_difference(
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
                )
            )
        elif metodo_func == "SDM":
            fi_final, psiX, iteracao, taxa_absorcao, taxa_fuga, duracao = med(
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
            )
        elif metodo_func == "MSD":
            fi_final, psiX, iteracao, taxa_absorcao, taxa_fuga, duracao = med_mod(
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
            )
        # ---------------------------------------------
        method = metodo_func
        primeiro_calculo = True
        return True  # Retorna True se nenhum erro ocorreu

    def coletar_dados(self):  # Função que coleta dados para serem utilizados
        global propriedades_1grupo, n_casas_decimais
        N = int(self.ui.ordem_quadratura.text())  # int
        cce = float(self.ui.gp1_esq_prescrita.text())
        ccd = float(self.ui.gp1_dir_prescrita.text())
        n_casas_decimais = int(self.ui.precisao_internas.text())
        precisao = float(f"1e-{n_casas_decimais+2}")

        tabela = self.ui.nodos_esp_zona  # Acessa a tabela de dados

        linhas = tabela.rowCount()  # Número de linhas
        colunas = tabela.columnCount()  # Número de colunas

        dados = []  # Coleta todos os dados
        for linha in range(linhas):
            dado_linha = []
            for coluna in range(colunas):
                item = tabela.item(linha, coluna)
                # Verifica se o item não é None antes de acessar o texto
                dado_linha.append(item.text() if item else "")
            dados.append(dado_linha)

        nodos = []  # Coleta os números de nodos digitados
        for coluna in range(colunas):
            nodos.append(dados[0][coluna])

        espessuras = []  # Coleta as espessuras das regiões
        for coluna in range(colunas):
            espessuras.append(dados[1][coluna])

        regioes = []  # Coleta os números da regiões
        for coluna in range(colunas):
            regioes.append(dados[2][coluna])

        esp_R = []  # Espessura da região
        NN = []  # Número de nodos
        reg = []

        n_regioes = int(self.ui.n_regioes.text())  # int
        for regiao in range(int(n_regioes)):
            esp_R.append(float(espessuras[regiao]))  # Separa todas as espessuras

            if float(nodos[regiao]).is_integer():
                NN.append(int(nodos[regiao]))  # Separa todos os números de nodos # int
            else:
                raise nodo_invalido

            reg.append(int(regioes[regiao]))  # Separa todos os números de regiões # int

        # PROPRIEDADES MATERIAIS 1G
        self.carregar_propriedades()
        sigmaT = propriedades_1grupo["Sigma T"]
        sigmaS0 = propriedades_1grupo["Sigma S0"]
        sigmaS1 = propriedades_1grupo["Sigma S1"]
        sigmaS2 = propriedades_1grupo["Sigma S2"]
        Qj = propriedades_1grupo["Fonte"]
        NiSigmaF = propriedades_1grupo["Ni*Sigma F"]

        for i in range(len(sigmaT)):
            sigmaT[i] = float(sigmaT[i])
            sigmaS0[i] = float(sigmaS0[i])
            sigmaS1[i] = float(sigmaS1[i])
            sigmaS2[i] = float(sigmaS2[i])
            Qj[i] = float(Qj[i])
            NiSigmaF[i] = float(NiSigmaF[i])

        return (
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
            reg,
            n_regioes,
            esp_R,
        )

    # Mesclar Gráficos
    def mesclar_graficos(self):
        combo_chart(junto=True)

    # Mostrar todos os gráficos gerados
    def mostrar_graficos(self):
        combo_chart(junto=False)

    # Função para aumentar o número de colunas da tabela de nodos, espessura e zonas
    def regioes(self):
        tabela = self.ui.nodos_esp_zona  # Define a tabela
        n_digitado = self.ui.n_regioes.text()  # Coleta o número de regiões digitado
        try:
            n_digitado = float(n_digitado)
            if n_digitado.is_integer() and n_digitado > 0:
                tabela.setColumnCount(
                    int(n_digitado)
                )  # Define o número de colunas da tabela
            else:
                raise ValueError
        except ValueError:
            self.ui.etapa.setText("ERRO VI-006")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-006: VALOR INVÁLIDO",
                "Certifique-se de que você escolheu um valor inteiro maior que zero para a quantidade de regiões.\n",
            )

    # Função para abrir a janela de propriedades 1G
    def abrir_propriedades_1G(self):
        self.janela_propriedades_1G = propriedades()
        self.janela_propriedades_1G.show()

    # Função para abrir a janela de resultados numéricos 1G
    def abrir_resultados_1G(self):
        global primeiro_calculo
        if primeiro_calculo == True:
            self.janela_resultados_1G = Resultados_Numericos_1G()
            self.janela_resultados_1G.show()
        else:
            QMessageBox.information(
                QMessageBox(),
                "ERRO AI-002: AÇÃO INVÁLIDA",
                "Certifique-se de que você rodou algum dos métodos para que sejam mostrados os resultados correspondentes.\n",
            )

    def abrir_ajuda(self):
        self.janela_ajuda = Janela_Instrucoes()
        self.janela_ajuda.show()


# RESULTADOS NUMÉRICOS 1G
class Resultados_Numericos_1G(QDialog):
    def __init__(self, *args, **argvs):
        super(Resultados_Numericos_1G, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.ui = Ui_resultados_1G()
        self.ui.setupUi(self)
        # Abrir gráfico ampliado
        self.ui.ampliar_grafico.clicked.connect(self.abrir_grafico)

        # Botão para mostrar os valores
        self.mostrar_resultados()

        # Botão de mostrar taxas
        self.ui.taxas.clicked.connect(self.abrir_janela)

    # Abrindo janela de taxas
    def abrir_janela(self):
        self.janela_taxas = taxas_resultados()
        self.janela_taxas.show()

    # Função para mostrar os resultados
    def mostrar_resultados(self):
        global primeiro_calculo, metodo, duracao, iteracao, n_casas_decimais

        # Adicionando número de iterações à label
        self.ui.iteracoes_1g.setText(f"{iteracao}")

        # Atualizando display com o tempo
        self.ui.duracao_calculo.setText(f"{duracao:.6f}")
        # Variáveis globais atualizadas
        global fi_final, dominio, psiX
        # GRÁFICO

        # Coleta o domínio e o caminho de salvamento do gráfico do MED
        save_path_grafico, dominio = main_graphic(
            NN, esp_R, fi_final, regioes, n_regioes, metodo, False
        )

        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(save_path_grafico)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.grafico.setScene(cena_grafico)

        # ---------------------------------------------
        # GRÁFICO DE INTENSIDADE

        # Coletando o caminho de salvamento do gráfico e as cores do valor máximo e mínimo
        save_path_intensidade, cor_max, cor_min = heat_graphic(fi_final)

        # Importando a figura e tornando-a em um item gráfico
        fig_int = QPixmap(save_path_intensidade)
        item_int = QGraphicsPixmapItem(fig_int)

        # Criando a cena para o espaço do gráfico
        cena_int = QGraphicsScene()
        cena_int.addItem(item_int)

        # Adicionando a cena ao espaço
        self.ui.grafico_intensidade.setScene(cena_int)

        # Tornando os quadrados da cor do máximo e mínimo
        self.ui.cor_maximo.setStyleSheet(f"background-color:{cor_max}")
        self.ui.cor_minimo.setStyleSheet(f"background-color:{cor_min}")
        # --------------------------------------------------------------
        # TABELA DE FLUXOS ESCALARES

        # Definindo a tabela de fluxos escalares
        tabela_escalares = self.ui.fluxos_escalares

        # Tornando-a com o número de colunas correto
        tabela_escalares.setColumnCount(len(fi_final))

        # Coletando o número de colunas
        colunas = tabela_escalares.columnCount()

        # Colocando os fluxos e domínio na tabela
        for fluxo in range(colunas):
            fluxo_escalar = tabela_escalares.item(0, fluxo)
            if fluxo_escalar:  # (Se tiver algo previamente digitado na célula)
                fluxo_escalar.setText(f"{fi_final[fluxo]:.{n_casas_decimais}e}")
            else:  # (Se não tiver algo previamente digitado na célula)
                tabela_escalares.setItem(
                    0,
                    fluxo,
                    QTableWidgetItem(f"{fi_final[fluxo]:.{n_casas_decimais}e}"),
                )

            dominio_fluxo = tabela_escalares.item(1, fluxo)
            if dominio_fluxo:  # (Se tiver algo previamente digitado na célula)
                dominio_fluxo.setText(f"{dominio[fluxo]:.6f}")
            else:  # (Se não tiver algo previamente digitado na célula)
                tabela_escalares.setItem(
                    1, fluxo, QTableWidgetItem(f"{dominio[fluxo]:.6f}")
                )

        # ---------------------------------------------
        # TABELA DE FLUXOS ANGULARES

        # Definindo a tabela de fluxos angulares
        tabela_angulares = self.ui.fluxos_angulares

        # Tornando-a com o número de colunas e linhas corretos
        tabela_angulares.setColumnCount(len(psiX))
        tabela_angulares.setRowCount(len(psiX[0]))

        # Coletando o número de colunas e linhas
        colunas = tabela_angulares.columnCount()
        linhas = tabela_angulares.rowCount()

        # CUIDADO: LÓGICA DE LINHAS X COLUNAS INVERTIDA: COLUNAS X LINHAS
        # Colocando os fluxos angulares na tabela
        for nodo in range(colunas):
            for m in range(linhas):
                fluxo_angular = tabela_angulares.item(m, nodo)
                if fluxo_angular:  # (Se tiver algo previamente digitado na célula)
                    fluxo_angular.setText(f"{psiX[nodo][m]:.{n_casas_decimais}e}")
                else:  # (Se não tiver algo previamente digitado na célula)
                    tabela_angulares.setItem(
                        m,
                        nodo,
                        QTableWidgetItem(f"{psiX[nodo][m]:.{n_casas_decimais}e}"),
                    )

    def abrir_grafico(self):
        global primeiro_calculo
        if primeiro_calculo == True:
            main_graphic(NN, esp_R, fi_final, regioes, n_regioes, method, True)
        else:
            self.ui.etapa.setText("ERRO AI-001")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO AI-001: AÇÃO INVÁLIDA",
                "Certifique-se de que você rodou algum dos métodos para que sejam mostrados os gráficos correspondentes.\n",
            )


class taxas_resultados(QDialog):
    def __init__(self, *args, **argvs):
        super(taxas_resultados, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.ui = Ui_taxas_resultado()
        self.ui.setupUi(self)

        self.mostrar_resultados()

    def mostrar_resultados(self):
        global taxa_absorcao, taxa_fuga, n_casas_decimais
        # TABELA ABSORÇÃO
        tabela_abs = self.ui.absorcao
        tabela_abs.setColumnCount(len(taxa_absorcao))
        for i in range(len(taxa_absorcao)):
            taxa = tabela_abs.item(0, i)
            if taxa:
                taxa.setText(f"{taxa_absorcao[i]:.{n_casas_decimais}e}")
            else:
                tabela_abs.setItem(
                    0, i, QTableWidgetItem(f"{taxa_absorcao[i]:.{n_casas_decimais}e}")
                )

        # TABELA FUGA
        soma_esp = sum(esp_R)
        self.ui.ponto_0_fuga.setText(f"{taxa_fuga[0]:.{n_casas_decimais}e}")
        self.ui.ponto_x_fuga.setText(f"{taxa_fuga[1]:.{n_casas_decimais}e}")
        self.ui.ponto_x.setText(f"{soma_esp}")


app = QApplication(sys.argv)
if QDialog.Accepted == True:
    window = dashboard_simulador()
    window.ensurePolished()
    window.show()
sys.exit(app.exec())
