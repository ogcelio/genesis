# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_simuladorlaFrtL.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 535)
        MainWindow.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionM_todos_2_Grupo = QAction(MainWindow)
        self.actionM_todos_2_Grupo.setObjectName("actionM_todos_2_Grupo")
        self.actionDD = QAction(MainWindow)
        self.actionDD.setObjectName("actionDD")
        self.actionDegrau_Caracter_stico = QAction(MainWindow)
        self.actionDegrau_Caracter_stico.setObjectName("actionDegrau_Caracter_stico")
        self.actionSpectral_Green_s_Function = QAction(MainWindow)
        self.actionSpectral_Green_s_Function.setObjectName(
            "actionSpectral_Green_s_Function"
        )
        self.actionReconstru_o = QAction(MainWindow)
        self.actionReconstru_o.setObjectName("actionReconstru_o")
        self.actionNumericos_1G = QAction(MainWindow)
        self.actionNumericos_1G.setObjectName("actionNumericos_1G")
        self.actionNumericos_2G = QAction(MainWindow)
        self.actionNumericos_2G.setObjectName("actionNumericos_2G")
        self.actionFisicos_Materiais_1G = QAction(MainWindow)
        self.actionFisicos_Materiais_1G.setObjectName("actionFisicos_Materiais_1G")
        self.actionFisicos_Materiais_2G = QAction(MainWindow)
        self.actionFisicos_Materiais_2G.setObjectName("actionFisicos_Materiais_2G")
        self.actionAjuda = QAction(MainWindow)
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionSDM = QAction(MainWindow)
        self.actionSDM.setObjectName("actionSDM")
        self.actionMSD = QAction(MainWindow)
        self.actionMSD.setObjectName("actionMSD")
        self.actionRelatorio = QAction(MainWindow)
        self.actionRelatorio.setObjectName("actionRelatorio")
        self.actionMesclarMetodos = QAction(MainWindow)
        self.actionMesclarMetodos.setObjectName("actionMesclarMetodos")
        self.actionMostrarGraficos = QAction(MainWindow)
        self.actionMostrarGraficos.setObjectName("actionMostrarGraficos")
        self.actionLimpar = QAction(MainWindow)
        self.actionLimpar.setObjectName("actionLimpar")
        self.actionSGF = QAction(MainWindow)
        self.actionSGF.setObjectName("actionSGF")
        self.actionRM = QAction(MainWindow)
        self.actionRM.setObjectName("actionRM")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 170, 661, 311))
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 16pt "Roboto";\n'
            "    border: 1px solid white;  /* Cor da borda preta */\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}\n"
            "\n"
            ""
        )
        self.nodos_esp_zona = QTableWidget(self.groupBox_7)
        if self.nodos_esp_zona.columnCount() < 1:
            self.nodos_esp_zona.setColumnCount(1)
        if self.nodos_esp_zona.rowCount() < 3:
            self.nodos_esp_zona.setRowCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(2, __qtablewidgetitem2)
        self.nodos_esp_zona.setObjectName("nodos_esp_zona")
        self.nodos_esp_zona.setGeometry(QRect(30, 130, 601, 131))
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nodos_esp_zona.sizePolicy().hasHeightForWidth()
        )
        self.nodos_esp_zona.setSizePolicy(sizePolicy)
        self.nodos_esp_zona.setMinimumSize(QSize(0, 0))
        self.nodos_esp_zona.setSizeIncrement(QSize(0, 0))
        self.nodos_esp_zona.setBaseSize(QSize(0, 0))
        self.nodos_esp_zona.setTabletTracking(False)
        self.nodos_esp_zona.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 8pt "Roboto";'
        )
        self.nodos_esp_zona.setIconSize(QSize(0, 0))
        self.grafico_espessura = QGraphicsView(self.groupBox_7)
        self.grafico_espessura.setObjectName("grafico_espessura")
        self.grafico_espessura.setGeometry(QRect(30, 270, 511, 21))
        self.grafico_espessura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.espessura_total = QLineEdit(self.groupBox_7)
        self.espessura_total.setObjectName("espessura_total")
        self.espessura_total.setGeometry(QRect(550, 270, 41, 20))
        self.espessura_total.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 9pt "Roboto";\ncolor: black;'
        )
        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(600, 270, 31, 16))
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet('color: white;\nfont: 10pt "Roboto";')
        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_8.setGeometry(QRect(140, 30, 381, 91))
        self.groupBox_8.setStyleSheet("")
        self.label_4 = QLabel(self.groupBox_8)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(20, 20, 71, 41))
        self.label_4.setStyleSheet('font: 700 8pt "Roboto";\ncolor: white;')
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(220, 20, 151, 41))
        self.label_5.setStyleSheet('font:  700 9pt "Roboto";\ncolor: white;')
        self.n_regioes = QLineEdit(self.groupBox_8)
        self.n_regioes.setObjectName("n_regioes")
        self.n_regioes.setGeometry(QRect(30, 60, 51, 20))
        self.n_regioes.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 8pt "Roboto";\ncolor: black;'
        )
        self.ok_regioes = QPushButton(self.groupBox_8)
        self.ok_regioes.setObjectName("ok_regioes")
        self.ok_regioes.setGeometry(QRect(110, 30, 41, 23))
        self.ok_regioes.setStyleSheet('font: 8pt "Roboto";\ncolor: white;')
        self.ordem_quadratura = QLineEdit(self.groupBox_8)
        self.ordem_quadratura.setObjectName("ordem_quadratura")
        self.ordem_quadratura.setGeometry(QRect(270, 60, 51, 20))
        self.ordem_quadratura.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 8pt "Roboto";\ncolor: black;'
        )
        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_9.setGeometry(QRect(400, 10, 281, 71))
        self.groupBox_9.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 16pt "Roboto";\n'
            "    border: 1px solid white;  /* Cor da borda preta */\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}\n"
            ""
        )
        self.precisao_internas = QLineEdit(self.groupBox_9)
        self.precisao_internas.setObjectName("precisao_internas")
        self.precisao_internas.setGeometry(QRect(220, 30, 51, 21))
        self.precisao_internas.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            'font: 8pt "Roboto";\n'
            "color: rgb(0,0,0);\n"
            ""
        )
        self.precisao_internas.setDragEnabled(False)
        self.label_16 = QLabel(self.groupBox_9)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(20, 30, 201, 16))
        self.label_16.setStyleSheet(
            'font: 700 11pt "Roboto";\ncolor: rgb(255,255,255);\n'
        )
        self.label_16.raise_()
        self.precisao_internas.raise_()
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 10, 341, 151))
        self.groupBox_6.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 16pt "Roboto";\n'
            "    border: 1px solid white;  /* Cor da borda preta */\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}"
        )
        self.groupBox_19 = QGroupBox(self.groupBox_6)
        self.groupBox_19.setObjectName("groupBox_19")
        self.groupBox_19.setGeometry(QRect(180, 30, 141, 101))
        self.groupBox_19.setStyleSheet('font: 700 12pt "Roboto";')
        self.label_20 = QLabel(self.groupBox_19)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(10, 20, 71, 16))
        self.label_20.setStyleSheet(
            'font: 700 12pt "Roboto";\ncolor: rgb(255,255,255)\n'
        )
        self.gp1_dir_prescrita = QLineEdit(self.groupBox_19)
        self.gp1_dir_prescrita.setObjectName("gp1_dir_prescrita")
        self.gp1_dir_prescrita.setGeometry(QRect(90, 20, 41, 20))
        font2 = QFont()
        font2.setFamilies(["Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.gp1_dir_prescrita.setFont(font2)
        self.gp1_dir_prescrita.setStyleSheet(
            "background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);"
        )
        self.gp1_dir_reflexiva = QRadioButton(self.groupBox_19)
        self.gp1_dir_reflexiva.setObjectName("gp1_dir_reflexiva")
        self.gp1_dir_reflexiva.setGeometry(QRect(20, 60, 101, 16))
        self.gp1_dir_reflexiva.setStyleSheet(
            'font: 700 11pt "Roboto";\ncolor: rgb(255,255,255);\n'
        )
        self.groupBox_18 = QGroupBox(self.groupBox_6)
        self.groupBox_18.setObjectName("groupBox_18")
        self.groupBox_18.setGeometry(QRect(20, 30, 141, 101))
        self.groupBox_18.setStyleSheet(
            'font: 700 12pt "Roboto";\ncolor: rgb(255,255,255);'
        )
        self.label_15 = QLabel(self.groupBox_18)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(10, 20, 71, 16))
        self.label_15.setStyleSheet(
            'font: 700 12pt "Roboto";\ncolor: rgb(255,255,255);\n'
        )
        self.gp1_esq_prescrita = QLineEdit(self.groupBox_18)
        self.gp1_esq_prescrita.setObjectName("gp1_esq_prescrita")
        self.gp1_esq_prescrita.setGeometry(QRect(90, 20, 41, 20))
        self.gp1_esq_prescrita.setFont(font2)
        self.gp1_esq_prescrita.setStyleSheet(
            "background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);"
        )
        self.gp1_esq_reflexiva = QRadioButton(self.groupBox_18)
        self.gp1_esq_reflexiva.setObjectName("gp1_esq_reflexiva")
        self.gp1_esq_reflexiva.setGeometry(QRect(20, 60, 91, 16))
        self.gp1_esq_reflexiva.setStyleSheet('font: 700 11pt "Roboto";\ncolor: white\n')
        self.groupBox_10 = QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.groupBox_10.setGeometry(QRect(400, 90, 281, 71))
        self.groupBox_10.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 16pt "Roboto";\n'
            "    border: 1px solid white;  /* Cor da borda preta */\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}\n"
            ""
        )
        self.etapa = QLineEdit(self.groupBox_10)
        self.etapa.setObjectName("etapa")
        self.etapa.setGeometry(QRect(50, 30, 191, 31))
        self.etapa.setFont(font2)
        self.etapa.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.etapa.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 700 12pt "Roboto";'
        )
        self.etapa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_1 = QGraphicsView(self.centralwidget)
        self.logo_1.setObjectName("logo_1")
        self.logo_1.setGeometry(QRect(740, 180, 181, 81))
        self.logo_1.setStyleSheet(
            "background-color: rgb(52, 73, 94);\nborder-radius: 20px;"
        )
        self.logo_2 = QGraphicsView(self.centralwidget)
        self.logo_2.setObjectName("logo_2")
        self.logo_2.setGeometry(QRect(720, 290, 221, 81))
        self.logo_2.setStyleSheet(
            "background-color: rgb(52, 73, 94);\nborder-radius: 20px;"
        )
        self.logo_3 = QGraphicsView(self.centralwidget)
        self.logo_3.setObjectName("logo_3")
        self.logo_3.setGeometry(QRect(740, 400, 181, 81))
        self.logo_3.setStyleSheet(
            "background-color: rgb(52, 73, 94);\nborder-radius: 20px;"
        )
        self.nome_simulador = QGraphicsView(self.centralwidget)
        self.nome_simulador.setObjectName("nome_simulador")
        self.nome_simulador.setGeometry(QRect(700, 40, 256, 91))
        self.nome_simulador.setStyleSheet(
            "background-color: rgb(52, 73, 94);\nborder-radius: 20px;"
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_10.raise_()
        self.groupBox_7.raise_()
        self.groupBox_9.raise_()
        self.groupBox_6.raise_()
        self.logo_1.raise_()
        self.logo_2.raise_()
        self.logo_3.raise_()
        self.nome_simulador.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 969, 19))
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        self.menubar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(168, 168, 168, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(0, 0, 0);\n"
            'font: 9pt "Arial";'
        )
        self.menuOpcoes = QMenu(self.menubar)
        self.menuOpcoes.setObjectName("menuOpcoes")
        self.menuCalcular = QMenu(self.menubar)
        self.menuCalcular.setObjectName("menuCalcular")
        self.menuM_tdos_1_Grupo = QMenu(self.menuCalcular)
        self.menuM_tdos_1_Grupo.setObjectName("menuM_tdos_1_Grupo")
        self.menuResultados = QMenu(self.menubar)
        self.menuResultados.setObjectName("menuResultados")
        self.menuPropriedades = QMenu(self.menubar)
        self.menuPropriedades.setObjectName("menuPropriedades")
        self.menuRelatorio_de_Simulacao = QMenu(self.menubar)
        self.menuRelatorio_de_Simulacao.setObjectName("menuRelatorio_de_Simulacao")
        self.menuHistorico = QMenu(self.menubar)
        self.menuHistorico.setObjectName("menuHistorico")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpcoes.menuAction())
        self.menubar.addAction(self.menuCalcular.menuAction())
        self.menubar.addAction(self.menuRelatorio_de_Simulacao.menuAction())
        self.menubar.addAction(self.menuResultados.menuAction())
        self.menubar.addAction(self.menuPropriedades.menuAction())
        self.menubar.addAction(self.menuHistorico.menuAction())
        self.menuOpcoes.addAction(self.actionAjuda)
        self.menuOpcoes.addAction(self.actionLimpar)
        self.menuOpcoes.addAction(self.actionSair)
        self.menuCalcular.addAction(self.menuM_tdos_1_Grupo.menuAction())
        self.menuM_tdos_1_Grupo.addAction(self.actionDD)
        self.menuM_tdos_1_Grupo.addAction(self.actionSDM)
        self.menuM_tdos_1_Grupo.addAction(self.actionMSD)
        self.menuM_tdos_1_Grupo.addAction(self.actionSGF)
        self.menuM_tdos_1_Grupo.addAction(self.actionRM)
        self.menuResultados.addAction(self.actionNumericos_1G)
        self.menuPropriedades.addAction(self.actionFisicos_Materiais_1G)
        self.menuRelatorio_de_Simulacao.addAction(self.actionRelatorio)
        self.menuHistorico.addAction(self.actionMesclarMetodos)
        self.menuHistorico.addAction(self.actionMostrarGraficos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("GENESIS", "GENESIS", None)
        )
        self.actionSair.setText(QCoreApplication.translate("MainWindow", "Sair", None))
        self.actionM_todos_2_Grupo.setText(
            QCoreApplication.translate("MainWindow", "M\u00e9todos 2 Grupo", None)
        )
        self.actionDD.setText(
            QCoreApplication.translate("MainWindow", "DD - Diamond Difference", None)
        )
        self.actionDegrau_Caracter_stico.setText(
            QCoreApplication.translate("MainWindow", "Degrau Caracter\u00edstico", None)
        )
        self.actionSpectral_Green_s_Function.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectral Green\u00b4s Function", None
            )
        )
        self.actionReconstru_o.setText(
            QCoreApplication.translate("MainWindow", "Reconstru\u00e7\u00e3o", None)
        )
        self.actionNumericos_1G.setText(
            QCoreApplication.translate("MainWindow", "Num\u00e9ricos - 1G", None)
        )
        self.actionNumericos_2G.setText(
            QCoreApplication.translate("MainWindow", "Num\u00e9ricos - 2G", None)
        )
        self.actionFisicos_Materiais_1G.setText(
            QCoreApplication.translate("MainWindow", "F\u00edsico Materiais - 1G", None)
        )
        self.actionFisicos_Materiais_2G.setText(
            QCoreApplication.translate("MainWindow", "F\u00edsico Materiais - 2G", None)
        )
        self.actionAjuda.setText(
            QCoreApplication.translate("MainWindow", "Ajuda", None)
        )
        self.actionSDM.setText(
            QCoreApplication.translate(
                "MainWindow", "SDM - Spectral Deterministic Method", None
            )
        )
        self.actionMSD.setText(
            QCoreApplication.translate(
                "MainWindow", "MSD - Modified Spectral Deterministic", None
            )
        )
        self.actionRelatorio.setText(
            QCoreApplication.translate("MainWindow", "Mostrar", None)
        )
        self.actionMesclarMetodos.setText(
            QCoreApplication.translate("MainWindow", "Mesclar M\u00e9todos", None)
        )
        self.actionMostrarGraficos.setText(
            QCoreApplication.translate("MainWindow", "Mostrar Gr\u00e1ficos", None)
        )
        self.actionLimpar.setText(
            QCoreApplication.translate("MainWindow", "Limpar Hist\u00f3rico", None)
        )
        self.actionSGF.setText(
            QCoreApplication.translate(
                "MainWindow", "SGF - Spectral Green's Function", None
            )
        )
        self.actionRM.setText(
            QCoreApplication.translate("MainWindow", "RM - Response Matrix", None)
        )
        self.groupBox_7.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Dom\u00ednio e Ordem de Quadratura", None
            )
        )
        ___qtablewidgetitem = self.nodos_esp_zona.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "Nodos", None)
        )
        ___qtablewidgetitem1 = self.nodos_esp_zona.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Espessura (cm)", None)
        )
        ___qtablewidgetitem2 = self.nodos_esp_zona.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Zona Material", None)
        )
        self.label_22.setText(QCoreApplication.translate("MainWindow", "(cm)", None))
        self.groupBox_8.setTitle("")
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Roboto\'; font-weight:700;">N\u00famero de </span></p>\n'
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Roboto\'; font-weight:700;">Regi\u00f5es</span></p></body></html>',
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Roboto\'; font-weight:700;">Ordem da Quadratura</span></p>\n'
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Roboto\'; font-weight:700;">de Gauss-Legendre</span></p></body></html>',
                None,
            )
        )
        self.n_regioes.setText(QCoreApplication.translate("MainWindow", "1", None))
        self.ok_regioes.setText(QCoreApplication.translate("MainWindow", "OK", None))
        self.ordem_quadratura.setText("")
        self.groupBox_9.setTitle(
            QCoreApplication.translate("MainWindow", "Precis\u00e3o", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", "N\u00famero de casas decimais:", None
            )
        )
        self.groupBox_6.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Condi\u00e7\u00f5es de Contorno", None
            )
        )
        self.groupBox_19.setTitle(
            QCoreApplication.translate("MainWindow", "Direita", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp1_dir_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp1_dir_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_18.setTitle(
            QCoreApplication.translate("MainWindow", "Esquerda", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp1_esq_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp1_esq_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_10.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Etapa da Simula\u00e7\u00e3o", None
            )
        )
        self.etapa.setText(
            QCoreApplication.translate("MainWindow", "N\u00c3O INICIADO", None)
        )
        self.menuOpcoes.setTitle(
            QCoreApplication.translate("MainWindow", "Op\u00e7\u00f5es", None)
        )
        self.menuCalcular.setTitle(
            QCoreApplication.translate("MainWindow", "Calcular", None)
        )
        self.menuM_tdos_1_Grupo.setTitle(
            QCoreApplication.translate("MainWindow", "M\u00e9tdos 1 Grupo", None)
        )
        self.menuResultados.setTitle(
            QCoreApplication.translate("MainWindow", "Resultados", None)
        )
        self.menuPropriedades.setTitle(
            QCoreApplication.translate("MainWindow", "Propriedades", None)
        )
        self.menuRelatorio_de_Simulacao.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Relat\u00f3rio de Simula\u00e7\u00e3o", None
            )
        )
        self.menuHistorico.setTitle(
            QCoreApplication.translate("MainWindow", "Hist\u00f3rico", None)
        )

    # retranslateUi
