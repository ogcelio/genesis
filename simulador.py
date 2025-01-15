import copy
import os
import sys
import time

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *

from dashboard_simulador import Ui_MainWindow  # Importando a dashboard do simulador
from gerando_grafico import (  # Importando funções de geração de gráficos
    gerar_tela,
    intensidade,
)
from metodo_dd_simples_final import (
    diamond_difference,  # Importando o Diamond Difference
)
from Propriedades_1G import Ui_Propriedades1G  # Importando a tela de propriedades 1G
from Resultados_Numericos_1G import Ui_Dialog  # Importando a tela de resultados 1G

# ---------------------------------------------------------------
# Propriedades materiais 1G
propriedades_1grupo = [
    ["1", "0.9500", "0", "0", "0", "0"],
    ["1", "0.9300", "0", "0", "0", "0"],
    ["1", "0.9800", "0", "0", "0", "0"],
    ["1", "0.9200", "0", "0", "0", "0"],
    ["1", "0.9100", "0", "0", "0", "0"],
    ["1", "0.8500", "0", "0", "0", "0"],
    ["0.2500", "0.0500", "0", "0", "0", "0.2200"],
    ["0.3333", "0.2333", "0", "0", "0", "0.3243"],
    ["0.2777", "0.1777", "0", "0", "0", "0.2042"],
    ["0.3333", "0.2333", "0", "0", "0", "0"],
]

# Criação de variáveis que serão mostradas
fi_final = []
dominio = []
psiX = []


class dashboard_simulador(QMainWindow):
    def __init__(self, *args, **argvs):
        super(dashboard_simulador, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_window()  # Centraliza a dashboard
        self.ui.ok_regioes.clicked.connect(self.regioes)  # Edita número de regiões
        self.ui.actionDiamond_Difference_DD.triggered.connect(
            self.iniciar_dd
        )  # Inicia o processo de cálculo
        self.ui.actionF_sicos_Materiais_1G.triggered.connect(
            self.abrir_propriedades_1G
        )  # Abre as propriedades 1G
        self.ui.actionNum_ricos_1G.triggered.connect(
            self.abrir_resultados_1G
        )  # Abre os resultados 1G

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

    def iniciar_dd(self):
        # Atualizando etapa
        self.ui.lineEdit.setText("CALCULANDO")
        QApplication.processEvents()  # Atualiza a tela

        inicio = time.time()  # Coleta o tempo inicial

        # Diamond Difference
        self.dd()

        final = time.time()  # Coleta o tempo final

        *_, Z, esp_Z = self.coletar_dados()  # Coletando número de regiões e espessura

        soma = 0
        for regiao in range(Z):  # fazendo a soma de todas as espessuras
            soma += esp_Z[regiao]

        self.ui.espessura_total.setText(
            f"{soma}"
        )  # Colocando a espessura total na label
        self.ui.grafico_espessura.setStyleSheet("background-color:blue")

        # Atualizando etapa
        self.ui.lineEdit.setText("FINALIZADO")
        QApplication.processEvents()  # Atualiza a tela

        # Atualizando display com o tempo
        duracao = abs(final - inicio)
        self.ui.lcdNumber.display(f"{duracao:.3f}")

    def coletar_dados(self):  # Função que coleta dados para serem utilizados
        N = int(self.ui.ordem_quadratura.text())
        cce = float(self.ui.gp1_esq_prescrita.text())
        ccd = float(self.ui.gp1_dir_prescrita.text())
        precisao = float(self.ui.precisao_internas.text())

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

        esp_Z = []  # Espessura da região
        NN = []  # Número de nodos
        Z = int(self.ui.n_regioes.text())  # Quantidade de regiões

        # PROPRIEDADES MATERIAIS 1G
        sigmaT = []
        sigmaS0 = []
        sigmaS1 = []
        sigmaS2 = []
        Qj = []
        NiSigmaF = []

        for regiao in range(Z):
            esp_Z.append(float(espessuras[regiao]))  # Separa todas as espessuras
            NN.append(int(nodos[regiao]))  # Separa todos os números de nodos

        for zona in range(linhas):  # Pegando os valores de cada componente
            sigmaT.append(float(propriedades_1grupo[zona][0]))
            sigmaS0.append(float(propriedades_1grupo[zona][1]))
            sigmaS1.append(float(propriedades_1grupo[zona][2]))
            sigmaS2.append(float(propriedades_1grupo[zona][3]))
            Qj.append(float(propriedades_1grupo[zona][4]))
            NiSigmaF.append(float(propriedades_1grupo[zona][5]))

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
            Z,
            esp_Z,
        )

    def dd(self):  # Roda o DD e gera o gráfico.
        # As variáveis precisam ser globais para que sejam utilizadas em outras funções
        global psiX, fi_final, dominio
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
            Z,
            esp_Z,
        ) = self.coletar_dados()  # Coleta os dados necessários

        # Roda o DD e coleta o fi final, psis finais e o número de iterações
        fi_final, psiX, iteracao = diamond_difference(
            N,
            NN[Z - 1],
            Z,
            esp_Z[Z - 1],
            sigmaT[Z - 1],
            sigmaS0[Z - 1],
            Qj[Z - 1],
            precisao,
            cce,
            ccd,
        )  # Considere apenas Z=1
        # ---------------------------------------------
        # GRÁFICO

        # Coleta o domínio e o caminho de salvamento do gráfico do DD
        save_path_grafico, dominio = gerar_tela(Z, NN[Z - 1], esp_Z[Z - 1], fi_final)

        # Importando a figura e tornando-a em um item gráfico
        fig_grafico = QPixmap(save_path_grafico)
        item_grafico = QGraphicsPixmapItem(fig_grafico)

        # Criando a cena para o espaço do gráfico
        cena_grafico = QGraphicsScene()
        cena_grafico.addItem(item_grafico)

        # Adicionando a cena ao espaço
        self.ui.grafico.setScene(cena_grafico)

        self.ui.i_internas.setText(
            f"{iteracao}"
        )  # Adicionando número de iterações à label
        # ---------------------------------------------
        # GRÁFICO DE INTENSIDADE

        # Coletando o caminho de salvamento do gráfico e as cores do valor máximo e mínimo
        save_path_intensidade, cor_max, cor_min = intensidade(fi_final)

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

    # Função para aumentar o número de colunas da tabela de nodos, espessura e zonas
    def regioes(self):
        tabela = self.ui.nodos_esp_zona  # Define a tabela
        n_digitado = int(
            self.ui.n_regioes.text()
        )  # Coleta o número de regiões digitado
        tabela.setColumnCount(n_digitado)  # Define o número de colunas da tabela

    # Função para abrir a janela de propriedades 1G
    def abrir_propriedades_1G(self):
        self.janela_propriedades_1G = Propriedades_1G()
        self.janela_propriedades_1G.show()

    # Função para abrir a janela de resultados numéricos 1G
    def abrir_resultados_1G(self):
        self.janela_resultados_1G = Resultados_Numericos_1G()
        self.janela_resultados_1G.show()


# PROPRIEDADES MATERIAIS 1 GRUPO
class Propriedades_1G(QDialog):
    def __init__(self, *args, **argvs):
        super(Propriedades_1G, self).__init__(*args, **argvs)
        self.ui = Ui_Propriedades1G()
        self.ui.setupUi(self)

        # Botão para atualizar os valores
        self.ui.pushButton.clicked.connect(self.atualizar_valores)

        global propriedades_1grupo  # Lista global para ser atualizada

        tabela = self.ui.tabela_valores  # Acessa a tabela de valores

        linhas = tabela.rowCount()  # Coleta o número de linhas
        colunas = tabela.columnCount()  # Coleta o numero de colunas

        # Colocando os valores predefinidos/atualizados na tabela
        for linha in range(linhas):
            for coluna in range(colunas):
                item = tabela.item(linha, coluna)
                item.setText(f"{propriedades_1grupo[linha][coluna]}")

    # Atualiza os valores da tabela ao clicar no botão
    def atualizar_valores(self):
        global propriedades_1grupo  # Lista global para ser atualizada
        tabela = self.ui.tabela_valores  # Acessa a tabela de valores

        linhas = tabela.rowCount()  # Coleta o número de linhas
        colunas = tabela.columnCount()  # Coleta o número de colunas

        # Atualiza os valores da lista que é de onde são tirados os valores
        # que serão printados na tabela
        for linha in range(linhas):
            for coluna in range(colunas):
                propriedades_1grupo[linha][coluna] = tabela.item(linha, coluna).text()


# RESULTADOS NUMÉRICOS 1G
class Resultados_Numericos_1G(QDialog):
    def __init__(self, *args, **argvs):
        super(Resultados_Numericos_1G, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Botão para mostrar os valores
        self.ui.mostrar_valores.clicked.connect(self.mostrar_resultados)

    # Função para mostrar os resultados
    def mostrar_resultados(self):
        # Variáveis globais atualizadas
        global fi_final, dominio, psiX

        # ---------------------------------------------
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
                fluxo_escalar.setText(f"{fi_final[fluxo]}")
            else:  # (Se não tiver algo previamente digitado na célula)
                tabela_escalares.setItem(
                    0, fluxo, QTableWidgetItem(f"{fi_final[fluxo]}")
                )

            dominio_fluxo = tabela_escalares.item(1, fluxo)
            if dominio_fluxo:  # (Se tiver algo previamente digitado na célula)
                dominio_fluxo.setText(f"{dominio[fluxo]}")
            else:  # (Se não tiver algo previamente digitado na célula)
                tabela_escalares.setItem(
                    1, fluxo, QTableWidgetItem(f"{dominio[fluxo]}")
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
                    fluxo_angular.setText(f"{psiX[nodo][m]}")
                else:  # (Se não tiver algo previamente digitado na célula)
                    tabela_angulares.setItem(
                        m, nodo, QTableWidgetItem(f"{psiX[nodo][m]}")
                    )


app = QApplication(sys.argv)
if QDialog.Accepted == True:
    window = dashboard_simulador()
    window.show()
sys.exit(app.exec_())
