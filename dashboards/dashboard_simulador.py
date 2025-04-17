# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_editada_IcpIdwDo.ui'
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
    QTime,
    QUrl,
    Qt,
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
    QLCDNumber,
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
        MainWindow.resize(1120, 700)
        MainWindow.setStyleSheet("background-color: rgb(205, 232, 210);")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionM_todos_2_Grupo = QAction(MainWindow)
        self.actionM_todos_2_Grupo.setObjectName("actionM_todos_2_Grupo")
        self.actionDiamond_Difference_DD = QAction(MainWindow)
        self.actionDiamond_Difference_DD.setObjectName("actionDiamond_Difference_DD")
        self.actionDegrau_Caracter_stico = QAction(MainWindow)
        self.actionDegrau_Caracter_stico.setObjectName("actionDegrau_Caracter_stico")
        self.actionSpectral_Green_s_Function = QAction(MainWindow)
        self.actionSpectral_Green_s_Function.setObjectName(
            "actionSpectral_Green_s_Function"
        )
        self.actionReconstru_o = QAction(MainWindow)
        self.actionReconstru_o.setObjectName("actionReconstru_o")
        self.actionNum_ricos_1G = QAction(MainWindow)
        self.actionNum_ricos_1G.setObjectName("actionNum_ricos_1G")
        self.actionNum_ricos_2G = QAction(MainWindow)
        self.actionNum_ricos_2G.setObjectName("actionNum_ricos_2G")
        self.actionF_sicos_Materiais_1G = QAction(MainWindow)
        self.actionF_sicos_Materiais_1G.setObjectName("actionF_sicos_Materiais_1G")
        self.action_SICO_mATERIAIS_2g = QAction(MainWindow)
        self.action_SICO_mATERIAIS_2g.setObjectName("action_SICO_mATERIAIS_2g")
        self.actionAjuda = QAction(MainWindow)
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionMED = QAction(MainWindow)
        self.actionMED.setObjectName("actionMED")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 461, 121))
        self.groupBox.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 14pt "Arial";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -3px; /* Ajuste vertical */\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 30, 151, 71))
        self.groupBox_2.setStyleSheet(
            'font: 75 11pt "Arial";\n' 'font: 700 11pt "Calibri";'
        )
        self.unigrupo = QRadioButton(self.groupBox_2)
        self.unigrupo.setObjectName("unigrupo")
        self.unigrupo.setGeometry(QRect(20, 20, 82, 17))
        self.unigrupo.setStyleSheet('font: 9pt "Arial";')
        self.duogrupo = QRadioButton(self.groupBox_2)
        self.duogrupo.setObjectName("duogrupo")
        self.duogrupo.setGeometry(QRect(20, 40, 82, 17))
        self.duogrupo.setStyleSheet('font: 9pt "Arial";')
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(180, 10, 251, 71))
        self.groupBox_3.setStyleSheet(
            'font: 11pt "Arial";\n' 'font: 700 11pt "Calibri";'
        )
        self.fonte_fixa = QRadioButton(self.groupBox_3)
        self.fonte_fixa.setObjectName("fonte_fixa")
        self.fonte_fixa.setGeometry(QRect(20, 20, 131, 17))
        self.fonte_fixa.setStyleSheet('font: 9pt "Arial";')
        self.autovalor = QRadioButton(self.groupBox_3)
        self.autovalor.setObjectName("autovalor")
        self.autovalor.setGeometry(QRect(20, 40, 181, 17))
        self.autovalor.setStyleSheet('font: 9pt "Arial";')
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 90, 101, 20))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet('font: 8pt "Arial";')
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(340, 90, 31, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('font: 8pt "Arial";')
        self.ok_potencia = QPushButton(self.groupBox)
        self.ok_potencia.setObjectName("ok_potencia")
        self.ok_potencia.setGeometry(QRect(390, 90, 41, 21))
        self.ok_potencia.setStyleSheet('font: 8pt "Arial";')
        self.potencia_gerada = QLineEdit(self.groupBox)
        self.potencia_gerada.setObjectName("potencia_gerada")
        self.potencia_gerada.setGeometry(QRect(300, 90, 31, 20))
        self.potencia_gerada.setStyleSheet(
            'font: 8pt "Arial";\n' "background-color: rgb(255, 255, 255);"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(670, 10, 251, 21))
        self.label_3.setStyleSheet('font: 700 14pt "Arial";')
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setGeometry(QRect(500, 40, 291, 131))
        self.groupBox_4.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Calibri";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "}\n"
            ""
        )
        self.groupBox_10 = QGroupBox(self.groupBox_4)
        self.groupBox_10.setObjectName("groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 20, 131, 101))
        self.groupBox_10.setStyleSheet('font: 700 12pt "Calibri";')
        self.label_6 = QLabel(self.groupBox_10)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(10, 20, 71, 16))
        self.label_6.setStyleSheet('font: 700 12pt "Calibri";')
        self.lineEdit_4 = QLineEdit(self.groupBox_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 20, 41, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.radioButton_5 = QRadioButton(self.groupBox_10)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setGeometry(QRect(30, 60, 91, 16))
        self.radioButton_5.setStyleSheet('font: 700 12pt "Calibri";')
        self.groupBox_11 = QGroupBox(self.groupBox_4)
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_11.setGeometry(QRect(150, 20, 131, 101))
        self.label_16 = QLabel(self.groupBox_11)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(10, 20, 71, 16))
        self.label_16.setStyleSheet('font: 700 12pt "Calibri";')
        self.lineEdit_12 = QLineEdit(self.groupBox_11)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(80, 20, 41, 20))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.radioButton_9 = QRadioButton(self.groupBox_11)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_9.setGeometry(QRect(30, 60, 81, 16))
        self.radioButton_9.setStyleSheet('font: 700 12pt "Calibri";')
        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 0, 291, 131))
        self.groupBox_5.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Calibri";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "}\n"
            ""
        )
        self.groupBox_12 = QGroupBox(self.groupBox_5)
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 20, 131, 101))
        self.groupBox_12.setStyleSheet('font: 700 12pt "Calibri";')
        self.label_8 = QLabel(self.groupBox_12)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(10, 20, 71, 16))
        self.label_8.setStyleSheet('font: 700 12pt "Calibri";')
        self.gp1_esq_prescrita = QLineEdit(self.groupBox_12)
        self.gp1_esq_prescrita.setObjectName("gp1_esq_prescrita")
        self.gp1_esq_prescrita.setGeometry(QRect(80, 20, 41, 20))
        font1 = QFont()
        font1.setFamilies(["Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.gp1_esq_prescrita.setFont(font1)
        self.gp1_esq_prescrita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gp1_esq_reflexiva = QRadioButton(self.groupBox_12)
        self.gp1_esq_reflexiva.setObjectName("gp1_esq_reflexiva")
        self.gp1_esq_reflexiva.setGeometry(QRect(30, 60, 91, 16))
        self.gp1_esq_reflexiva.setStyleSheet('font: 700 12pt "Calibri";')
        self.groupBox_13 = QGroupBox(self.groupBox_5)
        self.groupBox_13.setObjectName("groupBox_13")
        self.groupBox_13.setGeometry(QRect(150, 20, 131, 101))
        self.label_17 = QLabel(self.groupBox_13)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(10, 20, 71, 16))
        self.label_17.setStyleSheet('font: 700 12pt "Calibri";')
        self.gp1_dir_prescrita = QLineEdit(self.groupBox_13)
        self.gp1_dir_prescrita.setObjectName("gp1_dir_prescrita")
        self.gp1_dir_prescrita.setGeometry(QRect(80, 20, 41, 20))
        font2 = QFont()
        font2.setFamilies(["Calibri"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.gp1_dir_prescrita.setFont(font2)
        self.gp1_dir_prescrita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gp1_dir_reflexiva = QRadioButton(self.groupBox_13)
        self.gp1_dir_reflexiva.setObjectName("gp1_dir_reflexiva")
        self.gp1_dir_reflexiva.setGeometry(QRect(30, 60, 81, 16))
        self.gp1_dir_reflexiva.setStyleSheet('font: 700 12pt "Calibri";')
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 140, 461, 501))
        self.groupBox_6.setStyleSheet(
            "QGroupBox {\n"
            "    border: 1px solid black;  /* Borda de 1px */\n"
            "}\n"
            "\n"
            ""
        )
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(80, 10, 291, 20))
        self.grafico = QGraphicsView(self.groupBox_6)
        self.grafico.setObjectName("grafico")
        self.grafico.setGeometry(QRect(20, 30, 421, 371))
        self.grafico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.grafico_intensidade = QGraphicsView(self.groupBox_6)
        self.grafico_intensidade.setObjectName("grafico_intensidade")
        self.grafico_intensidade.setGeometry(QRect(20, 410, 421, 41))
        self.grafico_intensidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cor_maximo = QGraphicsView(self.groupBox_6)
        self.cor_maximo.setObjectName("cor_maximo")
        self.cor_maximo.setGeometry(QRect(20, 460, 31, 31))
        self.cor_maximo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(60, 460, 61, 31))
        font3 = QFont()
        font3.setFamilies(["Segoe UI"])
        self.label_20.setFont(font3)
        self.cor_minimo = QGraphicsView(self.groupBox_6)
        self.cor_minimo.setObjectName("cor_minimo")
        self.cor_minimo.setGeometry(QRect(150, 460, 31, 31))
        self.cor_minimo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(190, 460, 61, 31))
        self.label_21.setFont(font3)
        self.graphicsView_4 = QGraphicsView(self.groupBox_6)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(500, 440, 421, 41))
        self.graphicsView_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ampliar_grafico = QPushButton(self.groupBox_6)
        self.ampliar_grafico.setObjectName("ampliar_grafico")
        self.ampliar_grafico.setGeometry(QRect(310, 460, 131, 31))
        font4 = QFont()
        font4.setFamilies(["Arial"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.ampliar_grafico.setFont(font4)
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setGeometry(QRect(480, 180, 631, 301))
        font5 = QFont()
        font5.setFamilies(["Arial"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        self.groupBox_7.setFont(font5)
        self.groupBox_7.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 14pt "Arial";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -3px; /* Ajuste vertical */\n"
            "}\n"
            "\n"
            ""
        )
        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_8.setGeometry(QRect(180, 30, 271, 81))
        self.groupBox_8.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.groupBox_8)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(10, 13, 71, 31))
        self.label_4.setStyleSheet('font: 700 8pt "Calibri";')
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(200, 10, 61, 31))
        self.label_5.setStyleSheet('font:  700 9pt "Calibri";')
        self.n_regioes = QLineEdit(self.groupBox_8)
        self.n_regioes.setObjectName("n_regioes")
        self.n_regioes.setGeometry(QRect(20, 50, 41, 20))
        self.n_regioes.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";'
        )
        self.ok_regioes = QPushButton(self.groupBox_8)
        self.ok_regioes.setObjectName("ok_regioes")
        self.ok_regioes.setGeometry(QRect(90, 20, 41, 23))
        self.ok_regioes.setStyleSheet('font: 8pt "Arial";')
        self.ordem_quadratura = QLineEdit(self.groupBox_8)
        self.ordem_quadratura.setObjectName("ordem_quadratura")
        self.ordem_quadratura.setGeometry(QRect(210, 50, 41, 20))
        self.ordem_quadratura.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";'
        )
        self.nodos_esp_zona = QTableWidget(self.groupBox_7)
        if self.nodos_esp_zona.columnCount() < 1:
            self.nodos_esp_zona.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.nodos_esp_zona.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if self.nodos_esp_zona.rowCount() < 3:
            self.nodos_esp_zona.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.nodos_esp_zona.setVerticalHeaderItem(2, __qtablewidgetitem3)
        self.nodos_esp_zona.setObjectName("nodos_esp_zona")
        self.nodos_esp_zona.setGeometry(QRect(10, 120, 601, 141))
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
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";'
        )
        self.nodos_esp_zona.setIconSize(QSize(0, 0))
        self.grafico_espessura = QGraphicsView(self.groupBox_7)
        self.grafico_espessura.setObjectName("grafico_espessura")
        self.grafico_espessura.setGeometry(QRect(10, 270, 511, 21))
        self.grafico_espessura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.espessura_total = QLineEdit(self.groupBox_7)
        self.espessura_total.setObjectName("espessura_total")
        self.espessura_total.setGeometry(QRect(530, 270, 41, 20))
        self.espessura_total.setStyleSheet("background-color: rgb(255, 255, 255);\n" "")
        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(580, 270, 47, 16))
        font6 = QFont()
        font6.setPointSize(10)
        self.label_22.setFont(font6)
        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_9.setGeometry(QRect(480, 490, 361, 151))
        self.groupBox_9.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 14pt "Arial";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -3px; /* Ajuste vertical */\n"
            "}\n"
            ""
        )
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(30, 20, 47, 13))
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(10, 20, 111, 61))
        self.label_11.setStyleSheet('font: 8pt "Arial";')
        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(20, 90, 101, 41))
        self.label_12.setStyleSheet('font: 8pt "Arial";')
        self.i_internas = QLineEdit(self.groupBox_9)
        self.i_internas.setObjectName("i_internas")
        self.i_internas.setGeometry(QRect(130, 40, 51, 21))
        self.i_internas.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";'
        )
        self.i_externas = QLineEdit(self.groupBox_9)
        self.i_externas.setObjectName("i_externas")
        self.i_externas.setGeometry(QRect(130, 100, 51, 21))
        self.i_externas.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";'
        )
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(250, 20, 51, 16))
        self.label_13.setStyleSheet('font: 9pt "Calibri";')
        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(250, 70, 51, 20))
        self.label_14.setStyleSheet('font: 9pt "Calibri";')
        self.precisao_internas = QLineEdit(self.groupBox_9)
        self.precisao_internas.setObjectName("precisao_internas")
        self.precisao_internas.setGeometry(QRect(250, 40, 51, 21))
        self.precisao_internas.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";\n' ""
        )
        self.precisao_internas.setDragEnabled(False)
        self.precisao_externas = QLineEdit(self.groupBox_9)
        self.precisao_externas.setObjectName("precisao_externas")
        self.precisao_externas.setGeometry(QRect(250, 100, 51, 21))
        self.precisao_externas.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 8pt "Arial";\n' ""
        )
        self.groupBox_14 = QGroupBox(self.centralwidget)
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_14.setGeometry(QRect(800, 40, 291, 131))
        self.groupBox_14.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Calibri";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "}\n"
            ""
        )
        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 20, 131, 101))
        self.groupBox_15.setStyleSheet('font: 700 12pt "Calibri";')
        self.label_9 = QLabel(self.groupBox_15)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(10, 20, 71, 16))
        self.label_9.setStyleSheet('font: 700 12pt "Calibri";')
        self.gp2_esq_prescrita = QLineEdit(self.groupBox_15)
        self.gp2_esq_prescrita.setObjectName("gp2_esq_prescrita")
        self.gp2_esq_prescrita.setGeometry(QRect(80, 20, 41, 20))
        self.gp2_esq_prescrita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gp2_esq_reflexiva = QRadioButton(self.groupBox_15)
        self.gp2_esq_reflexiva.setObjectName("gp2_esq_reflexiva")
        self.gp2_esq_reflexiva.setGeometry(QRect(30, 60, 91, 16))
        self.gp2_esq_reflexiva.setStyleSheet('font: 700 12pt "Calibri";')
        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_16.setGeometry(QRect(150, 20, 131, 101))
        self.label_18 = QLabel(self.groupBox_16)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(10, 20, 71, 16))
        self.label_18.setStyleSheet('font: 700 12pt "Calibri";')
        self.gp2_dir_prescrita = QLineEdit(self.groupBox_16)
        self.gp2_dir_prescrita.setObjectName("gp2_dir_prescrita")
        self.gp2_dir_prescrita.setGeometry(QRect(80, 20, 41, 20))
        self.gp2_dir_prescrita.setFont(font2)
        self.gp2_dir_prescrita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gp2_dir_reflexiva = QRadioButton(self.groupBox_16)
        self.gp2_dir_reflexiva.setObjectName("gp2_dir_reflexiva")
        self.gp2_dir_reflexiva.setGeometry(QRect(30, 60, 81, 16))
        self.gp2_dir_reflexiva.setStyleSheet('font: 700 12pt "Calibri";')
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(890, 580, 181, 31))
        font7 = QFont()
        font7.setFamilies(["Segoe UI"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_7.setFont(font7)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setGeometry(QRect(880, 610, 201, 31))
        self.lcdNumber.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(255, 255, 255);\n" ""
        )
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(890, 490, 181, 21))
        self.label_19.setFont(font7)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(882, 520, 201, 31))
        font8 = QFont()
        font8.setFamilies(["Segoe UI"])
        font8.setPointSize(14)
        font8.setBold(True)
        self.lineEdit.setFont(font8)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 33))
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        self.menubar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(168, 168, 168, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(0, 0, 0);\n"
            'font: 9pt "Arial";'
        )
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuCalcular = QMenu(self.menubar)
        self.menuCalcular.setObjectName("menuCalcular")
        self.menuM_tdos_1_Grupo = QMenu(self.menuCalcular)
        self.menuM_tdos_1_Grupo.setObjectName("menuM_tdos_1_Grupo")
        self.menuM_todo_SGF = QMenu(self.menuM_tdos_1_Grupo)
        self.menuM_todo_SGF.setObjectName("menuM_todo_SGF")
        self.menuRelat_rios_da_simula_o = QMenu(self.menubar)
        self.menuRelat_rios_da_simula_o.setObjectName("menuRelat_rios_da_simula_o")
        self.menuResultados = QMenu(self.menubar)
        self.menuResultados.setObjectName("menuResultados")
        self.menuPropriedades = QMenu(self.menubar)
        self.menuPropriedades.setObjectName("menuPropriedades")
        self.menuPot_ncia = QMenu(self.menubar)
        self.menuPot_ncia.setObjectName("menuPot_ncia")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuCalcular.menuAction())
        self.menubar.addAction(self.menuRelat_rios_da_simula_o.menuAction())
        self.menubar.addAction(self.menuResultados.menuAction())
        self.menubar.addAction(self.menuPropriedades.menuAction())
        self.menubar.addAction(self.menuPot_ncia.menuAction())
        self.menuArquivo.addAction(self.actionSair)
        self.menuArquivo.addAction(self.actionAjuda)
        self.menuCalcular.addAction(self.menuM_tdos_1_Grupo.menuAction())
        self.menuCalcular.addAction(self.actionM_todos_2_Grupo)
        self.menuM_tdos_1_Grupo.addAction(self.menuM_todo_SGF.menuAction())
        self.menuM_tdos_1_Grupo.addAction(self.actionDiamond_Difference_DD)
        self.menuM_tdos_1_Grupo.addAction(self.actionDegrau_Caracter_stico)
        self.menuM_tdos_1_Grupo.addAction(self.actionMED)
        self.menuM_todo_SGF.addAction(self.actionSpectral_Green_s_Function)
        self.menuM_todo_SGF.addAction(self.actionReconstru_o)
        self.menuResultados.addAction(self.actionNum_ricos_1G)
        self.menuResultados.addAction(self.actionNum_ricos_2G)
        self.menuPropriedades.addAction(self.actionF_sicos_Materiais_1G)
        self.menuPropriedades.addAction(self.action_SICO_mATERIAIS_2g)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "SIMULADOR", None)
        )
        self.actionSair.setText(QCoreApplication.translate("MainWindow", "Sair", None))
        self.actionM_todos_2_Grupo.setText(
            QCoreApplication.translate("MainWindow", "M\u00e9todos 2 Grupo", None)
        )
        self.actionDiamond_Difference_DD.setText(
            QCoreApplication.translate("MainWindow", "Diamond Difference (DD)", None)
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
        self.actionNum_ricos_1G.setText(
            QCoreApplication.translate("MainWindow", "Num\u00e9ricos - 1G", None)
        )
        self.actionNum_ricos_2G.setText(
            QCoreApplication.translate("MainWindow", "Num\u00e9ricos - 2G", None)
        )
        self.actionF_sicos_Materiais_1G.setText(
            QCoreApplication.translate("MainWindow", "F\u00edsico Materiais - 1G", None)
        )
        self.action_SICO_mATERIAIS_2g.setText(
            QCoreApplication.translate("MainWindow", "F\u00edsico Materiais - 2G", None)
        )
        self.actionAjuda.setText(
            QCoreApplication.translate("MainWindow", "Ajuda", None)
        )
        self.actionMED.setText(QCoreApplication.translate("MainWindow", "MED", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Problema", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Energia", None)
        )
        self.unigrupo.setText(QCoreApplication.translate("MainWindow", "1 Grupo", None))
        self.duogrupo.setText(
            QCoreApplication.translate("MainWindow", "2 Grupos", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Possibilidade de fiss\u00e3o", None
            )
        )
        self.fonte_fixa.setText(
            QCoreApplication.translate("MainWindow", "N\u00e3o(Fonte Fixa)", None)
        )
        self.autovalor.setText(
            QCoreApplication.translate(
                "MainWindow", "Sim (Problema de Autovalor)", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt;">Pot\u00eancia Gerada:</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt;">MW</span></p></body></html>',
                None,
            )
        )
        self.ok_potencia.setText(QCoreApplication.translate("MainWindow", "OK", None))
        # if QT_CONFIG(tooltip)
        self.potencia_gerada.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><br/></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.potencia_gerada.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Condi\u00e7\u00f5es de Contorno</p></body></html>',
                None,
            )
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate("MainWindow", "Grupo 1", None)
        )
        self.groupBox_10.setTitle(
            QCoreApplication.translate("MainWindow", "Esquerda", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.radioButton_5.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_11.setTitle(
            QCoreApplication.translate("MainWindow", "Direita", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.radioButton_9.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_5.setTitle(
            QCoreApplication.translate("MainWindow", "Grupo 1", None)
        )
        self.groupBox_12.setTitle(
            QCoreApplication.translate("MainWindow", "Esquerda", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp1_esq_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp1_esq_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_13.setTitle(
            QCoreApplication.translate("MainWindow", "Direita", None)
        )
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp1_dir_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp1_dir_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_6.setTitle("")
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt;">Fluxo escalar m\u00e9dio de n\u00eautrons em um dom\u00ednio</span></p></body></html>',
                None,
            )
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">M\u00e1ximo</span></p></body></html>',
                None,
            )
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">M\u00ednimo</span></p></body></html>',
                None,
            )
        )
        self.ampliar_grafico.setText(
            QCoreApplication.translate("MainWindow", "Ampliar Gr\u00e1fico", None)
        )
        self.groupBox_7.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Dom\u00ednio e Ordem de Quadratura", None
            )
        )
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
                "</style></head><body style=\" font-family:'Calibri'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">N\u00famero de </span></p>\n'
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Regi\u00f5es</span></p></body></html>',
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
                "</style></head><body style=\" font-family:'Calibri'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Ordem da </span></p>\n'
                '<p align="center" style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Quadratura</span></p></body></html>',
                None,
            )
        )
        self.n_regioes.setText(QCoreApplication.translate("MainWindow", "1", None))
        self.ok_regioes.setText(QCoreApplication.translate("MainWindow", "OK", None))
        self.ordem_quadratura.setText("")
        ___qtablewidgetitem = self.nodos_esp_zona.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "1", None))
        ___qtablewidgetitem1 = self.nodos_esp_zona.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Nodos", None)
        )
        ___qtablewidgetitem2 = self.nodos_esp_zona.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Espessura(cm)", None)
        )
        ___qtablewidgetitem3 = self.nodos_esp_zona.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "Zona", None)
        )
        self.label_22.setText(QCoreApplication.translate("MainWindow", "(cm)", None))
        self.groupBox_9.setTitle(
            QCoreApplication.translate("MainWindow", "Processo Iterativo", None)
        )
        self.label_10.setText("")
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Calibri'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Itera\u00e7\u00f5es </span></p>\n'
                '<p align="center" style=" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Internas </span></p>\n'
                '<p align="center" style=" margin-top:1px; margin-bottom:1px; margin-lef'
                't:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">(Total)</span></p></body></html>',
                None,
            )
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Calibri'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Itera\u00e7\u00f5es </span></p>\n'
                '<p align="center" style=" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Calibri\'; font-weight:700;">Externas </span></p>\n'
                "",
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Precis\u00e3o", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Precis\u00e3o", None)
        )
        self.groupBox_14.setTitle(
            QCoreApplication.translate("MainWindow", "Grupo 2", None)
        )
        self.groupBox_15.setTitle(
            QCoreApplication.translate("MainWindow", "Esquerda", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp2_esq_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp2_esq_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.groupBox_16.setTitle(
            QCoreApplication.translate("MainWindow", "Direita", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", "Prescrita:", None)
        )
        self.gp2_dir_prescrita.setText(
            QCoreApplication.translate("MainWindow", "0", None)
        )
        self.gp2_dir_reflexiva.setText(
            QCoreApplication.translate("MainWindow", "Reflexiva", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Dura\u00e7\u00e3o do c\u00e1lculo (s):</p></body></html>',
                None,
            )
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Etapa:</p></body></html>',
                None,
            )
        )
        self.lineEdit.setText(
            QCoreApplication.translate("MainWindow", "N\u00c3O INICIADO", None)
        )
        self.menuArquivo.setTitle(
            QCoreApplication.translate("MainWindow", "Arquivo", None)
        )
        self.menuCalcular.setTitle(
            QCoreApplication.translate("MainWindow", "Calcular", None)
        )
        self.menuM_tdos_1_Grupo.setTitle(
            QCoreApplication.translate("MainWindow", "M\u00e9tdos 1 Grupo", None)
        )
        self.menuM_todo_SGF.setTitle(
            QCoreApplication.translate("MainWindow", "M\u00e9todo SGF", None)
        )
        self.menuRelat_rios_da_simula_o.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Relat\u00f3rios da simula\u00e7\u00e3o", None
            )
        )
        self.menuResultados.setTitle(
            QCoreApplication.translate("MainWindow", "Resultados", None)
        )
        self.menuPropriedades.setTitle(
            QCoreApplication.translate("MainWindow", "Propriedades", None)
        )
        self.menuPot_ncia.setTitle(
            QCoreApplication.translate("MainWindow", "Pot\u00eancia", None)
        )

    # retranslateUi
