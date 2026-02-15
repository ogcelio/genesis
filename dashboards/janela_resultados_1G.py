# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Resultados_Numericos_1GRBFZhY.ui'
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
    QDialog,
    QGraphicsView,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_resultados_1G(object):
    def setupUi(self, resultados_1G):
        if not resultados_1G.objectName():
            resultados_1G.setObjectName("resultados_1G")
        resultados_1G.resize(1033, 531)
        resultados_1G.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.groupBox_3 = QGroupBox(resultados_1G)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 451, 221))
        self.groupBox_3.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Roboto";\n'
            "	border: 1px solid white;\n"
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
        self.groupBox_3.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.fluxos_angulares = QTableWidget(self.groupBox_3)
        if self.fluxos_angulares.rowCount() < 4:
            self.fluxos_angulares.setRowCount(4)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.fluxos_angulares.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.fluxos_angulares.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font)
        self.fluxos_angulares.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font)
        self.fluxos_angulares.setVerticalHeaderItem(3, __qtablewidgetitem3)
        self.fluxos_angulares.setObjectName("fluxos_angulares")
        self.fluxos_angulares.setGeometry(QRect(10, 30, 431, 181))
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.fluxos_angulares.setFont(font1)
        self.fluxos_angulares.setStyleSheet(
            'font: 10pt "Roboto";\nbackground-color: rgb(255, 255, 255);'
        )
        self.groupBox_6 = QGroupBox(resultados_1G)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setGeometry(QRect(480, 10, 541, 511))
        self.groupBox_6.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Roboto";\n'
            "	border: 1px solid white;\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}"
        )
        self.grafico = QGraphicsView(self.groupBox_6)
        self.grafico.setObjectName("grafico")
        self.grafico.setGeometry(QRect(20, 30, 501, 371))
        self.grafico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.grafico_intensidade = QGraphicsView(self.groupBox_6)
        self.grafico_intensidade.setObjectName("grafico_intensidade")
        self.grafico_intensidade.setGeometry(QRect(20, 410, 501, 41))
        self.grafico_intensidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cor_maximo = QGraphicsView(self.groupBox_6)
        self.cor_maximo.setObjectName("cor_maximo")
        self.cor_maximo.setGeometry(QRect(20, 460, 31, 31))
        self.cor_maximo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(60, 460, 61, 31))
        font2 = QFont()
        font2.setFamilies(["Roboto"])
        font2.setPointSize(10)
        font2.setWeight(QFont.Medium)
        font2.setItalic(False)
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet('color: white;\nfont: 500 10pt "Roboto";')
        self.cor_minimo = QGraphicsView(self.groupBox_6)
        self.cor_minimo.setObjectName("cor_minimo")
        self.cor_minimo.setGeometry(QRect(150, 460, 31, 31))
        self.cor_minimo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(190, 460, 61, 31))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet('color: white;\nfont: 500 10pt "Roboto";')
        self.ampliar_grafico = QPushButton(self.groupBox_6)
        self.ampliar_grafico.setObjectName("ampliar_grafico")
        self.ampliar_grafico.setGeometry(QRect(380, 460, 131, 31))
        font3 = QFont()
        font3.setFamilies(["Roboto"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        self.ampliar_grafico.setFont(font3)
        self.ampliar_grafico.setStyleSheet('color: white;\nfont: 700 11pt "Roboto";')
        self.groupBox = QGroupBox(resultados_1G)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(10, 240, 451, 141))
        font4 = QFont()
        font4.setFamilies(["Roboto"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.groupBox.setFont(font4)
        self.groupBox.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Roboto";\n'
            "	border: 1px solid white;\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "\n"
            "}"
        )
        self.fluxos_escalares = QTableWidget(self.groupBox)
        if self.fluxos_escalares.rowCount() < 2:
            self.fluxos_escalares.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font)
        self.fluxos_escalares.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font)
        self.fluxos_escalares.setVerticalHeaderItem(1, __qtablewidgetitem5)
        self.fluxos_escalares.setObjectName("fluxos_escalares")
        self.fluxos_escalares.setGeometry(QRect(10, 30, 431, 101))
        self.fluxos_escalares.setFont(font1)
        self.fluxos_escalares.setStyleSheet(
            'font: 10pt "Roboto";\nbackground-color: rgb(255, 255, 255);'
        )
        self.taxas = QPushButton(resultados_1G)
        self.taxas.setObjectName("taxas")
        self.taxas.setGeometry(QRect(170, 480, 111, 31))
        self.taxas.setStyleSheet('color: white;\nfont: 500 10pt "Roboto";')
        self.groupBox_2 = QGroupBox(resultados_1G)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 390, 211, 71))
        self.groupBox_2.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Roboto";\n'
            "	border: 1px solid white;\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}"
        )
        self.iteracoes_1g = QLineEdit(self.groupBox_2)
        self.iteracoes_1g.setObjectName("iteracoes_1g")
        self.iteracoes_1g.setGeometry(QRect(40, 30, 131, 31))
        self.iteracoes_1g.setFont(font4)
        self.iteracoes_1g.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.iteracoes_1g.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 700 12pt "Roboto";'
        )
        self.iteracoes_1g.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4 = QGroupBox(resultados_1G)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 390, 211, 71))
        self.groupBox_4.setStyleSheet(
            "QGroupBox {\n"
            '	font: 700 12pt "Roboto";\n'
            "	border: 1px solid white;\n"
            "	border-radius: 8px;\n"
            "	margin-top: 1ex;\n"
            "}\n"
            ":title {\n"
            "color: white;\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "}"
        )
        self.duracao_calculo = QLineEdit(self.groupBox_4)
        self.duracao_calculo.setObjectName("duracao_calculo")
        self.duracao_calculo.setGeometry(QRect(40, 30, 131, 31))
        self.duracao_calculo.setFont(font4)
        self.duracao_calculo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.duracao_calculo.setStyleSheet(
            'background-color: rgb(255, 255, 255);\nfont: 700 12pt "Roboto";'
        )
        self.duracao_calculo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(resultados_1G)

        QMetaObject.connectSlotsByName(resultados_1G)

    # setupUi

    def retranslateUi(self, resultados_1G):
        resultados_1G.setWindowTitle(
            QCoreApplication.translate("resultados_1G", "Resultados - 1 Grupo", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate(
                "resultados_1G", "Fluxos Angulares [#/(cm\u00b2s)]", None
            )
        )
        ___qtablewidgetitem = self.fluxos_angulares.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("resultados_1G", "1", None)
        )
        ___qtablewidgetitem1 = self.fluxos_angulares.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("resultados_1G", "2", None)
        )
        ___qtablewidgetitem2 = self.fluxos_angulares.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("resultados_1G", "3", None)
        )
        ___qtablewidgetitem3 = self.fluxos_angulares.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("resultados_1G", "4", None)
        )
        self.groupBox_6.setTitle(
            QCoreApplication.translate(
                "resultados_1G", "Fluxo Escalar de n\u00eautrons no dom\u00ednio", None
            )
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "resultados_1G",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">M\u00e1ximo</span></p></body></html>',
                None,
            )
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "resultados_1G",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">M\u00ednimo</span></p></body></html>',
                None,
            )
        )
        self.ampliar_grafico.setText(
            QCoreApplication.translate("resultados_1G", "Ampliar Gr\u00e1fico", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate(
                "resultados_1G", "Fluxos Escalares [#/(cm\u00b2s)]", None
            )
        )
        ___qtablewidgetitem4 = self.fluxos_escalares.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("resultados_1G", "Fluxos", None)
        )
        ___qtablewidgetitem5 = self.fluxos_escalares.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("resultados_1G", "X (cm)", None)
        )
        self.taxas.setText(
            QCoreApplication.translate("resultados_1G", "Mostrar Taxas", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate(
                "resultados_1G", "N\u00famero de Itera\u00e7\u00f5es", None
            )
        )
        self.iteracoes_1g.setText(
            QCoreApplication.translate("resultados_1G", "0", None)
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate(
                "resultados_1G", "Dura\u00e7\u00e3o do C\u00e1lculo (s):", None
            )
        )
        self.duracao_calculo.setText(
            QCoreApplication.translate("resultados_1G", "0", None)
        )

    # retranslateUi
