# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_taxasnoRHYa.ui'
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
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_taxas_resultado(object):
    def setupUi(self, taxas_resultado):
        if not taxas_resultado.objectName():
            taxas_resultado.setObjectName("taxas_resultado")
        taxas_resultado.resize(527, 281)
        taxas_resultado.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.groupBox = QGroupBox(taxas_resultado)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 511, 111))
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
            "}"
        )
        self.absorcao = QTableWidget(self.groupBox)
        if self.absorcao.columnCount() < 1:
            self.absorcao.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.absorcao.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if self.absorcao.rowCount() < 1:
            self.absorcao.setRowCount(1)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.absorcao.setVerticalHeaderItem(0, __qtablewidgetitem1)
        self.absorcao.setObjectName("absorcao")
        self.absorcao.setGeometry(QRect(10, 30, 491, 71))
        self.absorcao.setFont(font)
        self.absorcao.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.groupBox_2 = QGroupBox(taxas_resultado)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 511, 141))
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
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(20, 30, 101, 31))
        font1 = QFont()
        font1.setFamilies(["Segoe UI"])
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ponto_0_fuga = QLineEdit(self.groupBox_2)
        self.ponto_0_fuga.setObjectName("ponto_0_fuga")
        self.ponto_0_fuga.setGeometry(QRect(130, 30, 121, 31))
        self.ponto_0_fuga.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ponto_x_fuga = QLineEdit(self.groupBox_2)
        self.ponto_x_fuga.setObjectName("ponto_x_fuga")
        self.ponto_x_fuga.setGeometry(QRect(200, 90, 121, 31))
        self.ponto_x_fuga.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ponto_x = QLineEdit(self.groupBox_2)
        self.ponto_x.setObjectName("ponto_x")
        self.ponto_x.setGeometry(QRect(80, 90, 71, 31))
        self.ponto_x.setStyleSheet(
            "background-color: rgb(52, 73, 94);\n" "color: rgb(255, 255, 255);"
        )
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(20, 90, 61, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(160, 90, 31, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")

        self.retranslateUi(taxas_resultado)

        QMetaObject.connectSlotsByName(taxas_resultado)

    # setupUi

    def retranslateUi(self, taxas_resultado):
        taxas_resultado.setWindowTitle(
            QCoreApplication.translate(
                "taxas_resultado", "Resultados das Taxas - 1 Grupo", None
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate(
                "taxas_resultado", "Taxa de Absor\u00e7\u00e3o", None
            )
        )
        ___qtablewidgetitem = self.absorcao.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("taxas_resultado", "1", None)
        )
        ___qtablewidgetitem1 = self.absorcao.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("taxas_resultado", "Taxas", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("taxas_resultado", "Taxa de Fuga", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "taxas_resultado",
                '<html><head/><body><p><span style=" font-size:10pt;">No ponto 0 cm = </span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "taxas_resultado",
                '<html><head/><body><p><span style=" font-size:10pt;">No ponto</span></p></body></html>',
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "taxas_resultado",
                '<html><head/><body><p><span style=" font-size:10pt;">cm =</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
