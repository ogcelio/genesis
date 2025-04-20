# OBJETIVOS:
# MELHORAR A EFICIÊNCIA DO CÓDIGO;
# MUDAR A APARÊNCIA DA INTERFACE DO SIMULADOR;
# TORNAR A FUNÇÃO SEM ERROS NUMA FUNÇÃO "GLOBAL", QUE VERIFICA OS ERROS E RETORNA O ERRO ESPECÍFICO PRESENTE NO ARQUIVO "ERROS";
# ADICIONAR AS FUNÇÕES MULTIGRUPO;
# ADICIONAR UMA FUNÇÃO EM QUE PERMITA MESCLAR DOIS GRÁFICOS DE DOIS MÉTODOS DIFERENTES, PARA QUE ELES SEJAM COMPARADOS;
# ADICIONAR UMA JANELA DE "PREFERÊNCIAS" NO SIMULADOR, EM QUE NELA ACONTECERÁ:
#   1- ESCOLHA ENTRE TEMA CLARO E ESCURO;
#   2- CONFIGURAÇÕES DO SIMULADOR;
#   3- MAIS OPÇÕES.
# ADICIONAR NOVOS MÉTODOS:
#   1- MED MODIFICADO;
#   2- SPECTRAL GREEN'S FUNCTION (SGF).


import copy
import os
import sys
import time
import json
import numpy as np

from PySide6 import QtCore, QtGui, QtWidgets

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QPalette, QColor

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
from dashboards.Propriedades_1G import (
    Ui_Propriedades1G,  # Importando a tela de propriedades 1G
)
from dashboards.Resultados_Numericos_1G import (
    Ui_Dialog,  # Importando a tela de resultados 1G
)
from metodos.Diamond_Difference.graficos_dd import (  # Importando funções de geração de gráficos
    gerar_tela_dd,
    grafico_regioes,
    intensidade,
)
from metodos.Diamond_Difference.metodo_dd import (
    diamond_difference,  # Importando o Diamond Difference
)
from metodos.MED.graficos_med import (
    gerar_tela_med,
)  # Importando funções de geração de gráficos
from metodos.MED.metodo_med import med  # Importando o MED
from mensagens.erros import *
from dashboards.janela_ajuda import Janela_Instrucoes

# Criação de variáveis que serão mostradas
fi_final, dominio, psiX, taxa_absorcao, taxa_fuga, regioes, NN = ([] for _ in range(7))
path = "dados\\propriedades.json"
with open(path, "r", encoding="utf8") as file:
    propriedades_1grupo = json.load(file)
esp_R = 0
n_regioes = 0

primeiro_calculo = False


class dashboard_simulador(QMainWindow):
    def __init__(self, *args, **argvs):
        super(dashboard_simulador, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        # Define o estilo Fusion para mudar a paleta
        app.setStyle("Fusion")

        # Criar uma paleta clara
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.black)
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(0, 122, 204))
        palette.setColor(QPalette.Highlight, QColor(0, 122, 204))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        app.setPalette(palette)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_window()  # Centraliza a dashboard
        self.ui.ok_regioes.clicked.connect(self.regioes)  # Edita número de regiões
        self.ui.actionDiamond_Difference_DD.triggered.connect(
            self.iniciar_dd
        )  # Inicia o processo de cálculo do DD
        self.ui.actionMED.triggered.connect(
            self.iniciar_med
        )  # Inicia o processo de cálculo do MED
        self.ui.actionF_sicos_Materiais_1G.triggered.connect(
            self.abrir_propriedades_1G
        )  # Abre as propriedades 1G
        self.ui.actionNum_ricos_1G.triggered.connect(
            self.abrir_resultados_1G
        )  # Abre os resultados 1G
        self.ui.actionSair.triggered.connect(
            self.close
        )  # Fecha a janela ao clicar em sair
        self.ui.ampliar_grafico.clicked.connect(
            self.abrir_grafico
        )  # Abre uma janela onde se pode manipular o gráfico gerado
        self.ui.actionAjuda.triggered.connect(
            self.abrir_ajuda
        )  # Abre a janela de ajuda
        self.ui.lineEdit.setReadOnly(
            True
        )  # Impede que a caixa de texto de "etapa" seja editada pelo usuário

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
        global esp_R  # Espessuras globais para que sejam utilizadas posteriormente

        # Atualizando etapa
        self.ui.lineEdit.setText("CALCULANDO")
        QApplication.processEvents()  # Atualiza a tela

        inicio = time.time()  # Coleta o tempo inicial

        # Diamond Difference
        sem_erros = self.dd()
        if (
            sem_erros != True
        ):  # Se sem_erros for diferente de True, o método não finaliza
            return

        final = time.time()  # Coleta o tempo final

        *_, Z, n_regioes, esp_R = (
            self.coletar_dados()
        )  # Coletando número de regiões e espessura
        soma = sum(esp_R)  # Fazendo a soma de todas as espessuras

        self.ui.espessura_total.setText(
            f"{soma}"
        )  # Colocando a espessura total na label

        # GRÁFICO -----------------------------------

        # Coleta o domínio e o caminho de salvamento do gráfico do DD
        save_path_grafico = grafico_regioes(esp_R)

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
        self.ui.lineEdit.setText("FINALIZADO")
        QApplication.processEvents()  # Atualiza a tela

        # Atualizando display com o tempo
        duracao = abs(final - inicio)
        self.ui.lcdNumber.display(f"{duracao:.3f}")

    def iniciar_med(self):
        global esp_R  # Espessuras globais para que sejam utilizadas posteriormente

        # Atualizando etapa
        self.ui.lineEdit.setText("CALCULANDO")
        QApplication.processEvents()  # Atualiza a tela

        inicio = time.time()  # Coleta o tempo inicial

        # Diamond Difference
        sem_erros = self.med_calculo()
        if (
            sem_erros != True
        ):  # Se sem_erros for diferente de True, o método não finaliza
            return

        final = time.time()  # Coleta o tempo final

        *_, Z, n_regioes, esp_R = (
            self.coletar_dados()
        )  # Coletando número de regiões e espessura
        soma = sum(esp_R)  # Fazendo a soma de todas as espessuras

        self.ui.espessura_total.setText(
            f"{soma}"
        )  # Colocando a espessura total na label

        # GRÁFICO -----------------------------------

        # Coleta o domínio e o caminho de salvamento do gráfico do MED
        save_path_grafico = grafico_regioes(esp_R)

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
        self.ui.lineEdit.setText("FINALIZADO")
        QApplication.processEvents()  # Atualiza a tela

        # Atualizando display com o tempo
        duracao = abs(final - inicio)
        self.ui.lcdNumber.display(f"{duracao:.3f}")

    def coletar_dados(self):  # Função que coleta dados para serem utilizados
        N = int(self.ui.ordem_quadratura.text())  # int
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

    def med_calculo(self):
        # As variáveis precisam ser globais para que sejam utilizadas em outras funções
        global psiX, fi_final, dominio, taxa_absorcao, taxa_fuga, n_regioes, regioes, NN, primeiro_calculo

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
            self.ui.lineEdit.setText("ERRO VI-001")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-001: VALOR INVÁLIDO",
                "Certifique-se de que você digitou todos os dados corretamente, sem caixas em branco.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False  # Retorna False se algum erro ocorrer
        except quadratura_invalida:
            self.ui.lineEdit.setText("ERRO VI-002")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-002: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor par, inteiro e maior que zero para a ordem da quadratura.",
            )
            return False
        except nodo_invalido:
            self.ui.lineEdit.setText("ERRO VI-003")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-003: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor inteiro e maior que zero para o número de nodos de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except espessura_zero:
            self.ui.lineEdit.setText("ERRO VI-004")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-004: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor maior que zero para a espessura de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except regiao_invalida:
            self.ui.lineEdit.setText("ERRO VI-005")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-005: VALOR INVÁLIDO",
                f"Certifique-se de que você escolheu um valor inteiro para a zona entre 1 e {len(sigmaT)}.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False

        # Roda o DD e coleta o fi final, psis finais e o número de iterações
        fi_final, psiX, iteracao, taxa_absorcao, taxa_fuga = med(
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
        # GRÁFICO

        # Coleta o domínio e o caminho de salvamento do gráfico do MED
        save_path_grafico, dominio = gerar_tela_med(
            NN, esp_R, fi_final, regioes, n_regioes, False
        )

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

        primeiro_calculo = True
        return True  # Retorna True se nenhum erro ocorreu

    def dd(self):  # Roda o DD e gera o gráfico.
        # As variáveis precisam ser globais para que sejam utilizadas em outras funções
        global psiX, fi_final, dominio, taxa_absorcao, taxa_fuga, n_regioes, regioes, NN, primeiro_calculo

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
            self.ui.lineEdit.setText("ERRO VI-001")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-001: VALOR INVÁLIDO",
                "Certifique-se de que você digitou todos os dados corretamente, sem caixas em branco.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False  # Retorna False se algum erro ocorrer
        except quadratura_invalida:
            self.ui.lineEdit.setText("ERRO VI-002")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-002: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor par, inteiro e maior que zero para a ordem da quadratura.",
            )
            return False
        except nodo_invalido:
            self.ui.lineEdit.setText("ERRO VI-003")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-003: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor inteiro e maior que zero para o número de nodos de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except espessura_zero:
            self.ui.lineEdit.setText("ERRO VI-004")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-004: VALOR INVÁLIDO",
                "Certifique-se de que você digitou um valor maior que zero para a espessura de cada uma das regiões.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False
        except regiao_invalida:
            self.ui.lineEdit.setText("ERRO VI-005")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-005: VALOR INVÁLIDO",
                f"Certifique-se de que você escolheu um valor inteiro para a zona entre 1 e {len(sigmaT)}.\n"
                "\nOBS.: Não deixe nenhuma caixa selecionada. Isso pode fazer com que a interface não reconheça o que está digitado nela.",
            )
            return False

        # Roda o DD e coleta o fi final, psis finais e o número de iterações
        fi_final, psiX, iteracao, taxa_absorcao, taxa_fuga = diamond_difference(
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
        # GRÁFICO

        # Coleta o domínio e o caminho de salvamento do gráfico do DD
        save_path_grafico, dominio = gerar_tela_dd(
            NN, esp_R, fi_final, regioes, n_regioes, False
        )

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

        primeiro_calculo = True
        return True  # Retorna True se nenhum erro ocorreu

    def abrir_grafico(self):
        global primeiro_calculo
        if primeiro_calculo == True:
            gerar_tela_dd(NN, esp_R, fi_final, regioes, n_regioes, True)
        else:
            QMessageBox.information(
                QMessageBox(),
                "ERRO AI-001: AÇÃO INVÁLIDA",
                "Certifique-se de que você rodou algum dos métodos para que sejam mostrados os gráficos correspondentes.\n",
            )

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
            self.ui.lineEdit.setText("ERRO VI-006")
            QApplication.processEvents()  # Atualiza a tela
            QMessageBox.information(
                QMessageBox(),
                "ERRO VI-006: VALOR INVÁLIDO",
                "Certifique-se de que você escolheu um valor inteiro maior que zero para a quantidade de regiões.\n",
            )

    # Função para abrir a janela de propriedades 1G
    def abrir_propriedades_1G(self):
        self.janela_propriedades_1G = Propriedades_1G()
        self.janela_propriedades_1G.show()

    # Função para abrir a janela de resultados numéricos 1G
    def abrir_resultados_1G(self):
        self.janela_resultados_1G = Resultados_Numericos_1G()
        self.janela_resultados_1G.show()

    def abrir_ajuda(self):
        self.janela_ajuda = Janela_Instrucoes()
        self.janela_ajuda.show()


# PROPRIEDADES MATERIAIS 1 GRUPO
class Propriedades_1G(QDialog):
    def __init__(self, *args, **argvs):
        super(Propriedades_1G, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.ui = Ui_Propriedades1G()
        self.ui.setupUi(self)

        # Botão para atualizar os valores
        self.ui.pushButton.clicked.connect(self.atualizar_valores)

        global propriedades_1grupo  # Lista global para ser atualizada

        tabela = self.ui.tabela_valores  # Acessa a tabela de valores

        linhas = tabela.rowCount()  # Coleta o número de linhas
        colunas = tabela.columnCount()  # Coleta o numero de colunas

        # Colocando os valores predefinidos/atualizados na tabela
        for coluna, tipo_valor in enumerate(propriedades_1grupo.values()):
            for linha, valor in enumerate(tipo_valor):
                item = tabela.item(linha, coluna)
                item.setText(f"{valor}")

    # Atualiza os valores da tabela ao clicar no botão
    def atualizar_valores(self):
        global propriedades_1grupo  # Lista global para ser atualizada
        tabela = self.ui.tabela_valores  # Acessa a tabela de valores

        linhas = tabela.rowCount()  # Coleta o número de linhas
        colunas = tabela.columnCount()  # Coleta o número de colunas

        # Atualiza os valores da lista que é de onde são tirados os valores
        # que serão printados na tabela

        for coluna, chave in enumerate(propriedades_1grupo.keys()):
            dados = []
            for linha in range(linhas):
                dados.append(tabela.item(linha, coluna).text())
            propriedades_1grupo[chave] = dados

        path = "dados\\propriedades.json"
        with open(path, "w+", encoding="utf8") as file:
            json.dump(propriedades_1grupo, file, indent=2)


# RESULTADOS NUMÉRICOS 1G
class Resultados_Numericos_1G(QDialog):
    def __init__(self, *args, **argvs):
        super(Resultados_Numericos_1G, self).__init__(*args, **argvs)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Botão para mostrar os valores
        self.ui.mostrar_valores.clicked.connect(self.mostrar_resultados)

    # Função para mostrar os resultados
    def mostrar_resultados(self):
        global primeiro_calculo
        if primeiro_calculo == True:
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
                    dominio_fluxo.setText(f"{dominio[fluxo]:.2f}")
                else:  # (Se não tiver algo previamente digitado na célula)
                    tabela_escalares.setItem(
                        1, fluxo, QTableWidgetItem(f"{dominio[fluxo]:.2f}")
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

            # TABELA ABSORÇÃO
            tabela_abs = self.ui.absorcao
            tabela_abs.setColumnCount(len(taxa_absorcao))
            for i in range(len(taxa_absorcao)):
                taxa = tabela_abs.item(0, i)
                if taxa:
                    taxa.setText(f"{taxa_absorcao[i]:.4e}")
                else:
                    tabela_abs.setItem(
                        0, i, QTableWidgetItem(f"{taxa_absorcao[i]:.4e}")
                    )

            # TABELA FUGA
            soma_esp = sum(esp_R)
            self.ui.ponto_0_fuga.setText(f"{taxa_fuga[0]:.4e}")
            self.ui.ponto_x_fuga.setText(f"{taxa_fuga[1]:.4e}")
            self.ui.ponto_x.setText(f"{soma_esp}")
        else:
            QMessageBox.information(
                QMessageBox(),
                "ERRO AI-002: AÇÃO INVÁLIDA",
                "Certifique-se de que você rodou algum dos métodos para que sejam mostrados os resultados correspondentes.\n",
            )


app = QApplication(sys.argv)
if QDialog.Accepted == True:
    window = dashboard_simulador()
    window.show()
sys.exit(app.exec())
