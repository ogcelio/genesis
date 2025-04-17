# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Resultados_Numericos_1GdEPPgJ.ui'
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
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(911, 480)
        self.fundo = QLabel(Dialog)
        self.fundo.setObjectName("fundo")
        self.fundo.setGeometry(QRect(-110, -120, 1051, 721))
        self.fundo.setStyleSheet("background-color: rgb(205, 232, 210);")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 451, 131))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(10)
        font.setWeight(QFont.Medium)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(
            "QGroupBox {\n"
            '	font: 500 10pt "Segoe UI";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -5px; /* Ajuste vertical */\n"
            "}"
        )
        self.fluxos_escalares = QTableWidget(self.groupBox)
        if self.fluxos_escalares.rowCount() < 2:
            self.fluxos_escalares.setRowCount(2)
        font1 = QFont()
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1)
        self.fluxos_escalares.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1)
        self.fluxos_escalares.setVerticalHeaderItem(1, __qtablewidgetitem1)
        self.fluxos_escalares.setObjectName("fluxos_escalares")
        self.fluxos_escalares.setGeometry(QRect(5, 20, 441, 101))
        self.fluxos_escalares.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 141, 31))
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 190, 451, 111))
        self.groupBox_2.setStyleSheet(
            "QGroupBox {\n"
            '	font: 500 10pt "Segoe UI";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -4px; /* Ajuste vertical */\n"
            "}\n"
            ""
        )
        self.absorcao = QTableWidget(self.groupBox_2)
        if self.absorcao.columnCount() < 1:
            self.absorcao.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.absorcao.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        if self.absorcao.rowCount() < 1:
            self.absorcao.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1)
        self.absorcao.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.absorcao.setObjectName("absorcao")
        self.absorcao.setGeometry(QRect(10, 20, 431, 81))
        self.absorcao.setFont(font1)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 50, 431, 381))
        self.groupBox_3.setStyleSheet(
            "QGroupBox {\n"
            '	font: 500 10pt "Segoe UI";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -5px; /* Ajuste vertical */\n"
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1)
        self.fluxos_angulares.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1)
        self.fluxos_angulares.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1)
        self.fluxos_angulares.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1)
        self.fluxos_angulares.setVerticalHeaderItem(3, __qtablewidgetitem7)
        self.fluxos_angulares.setObjectName("fluxos_angulares")
        self.fluxos_angulares.setGeometry(QRect(10, 20, 411, 351))
        self.fluxos_angulares.setFont(font1)
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 310, 451, 121))
        self.groupBox_4.setStyleSheet(
            "QGroupBox {\n"
            '	font: 500 10pt "Segoe UI";\n'
            "    border: 1px solid black;  /* Cor da borda preta */\n"
            "}\n"
            ":title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top left; /* Posi\u00e7\u00e3o no canto superior esquerdo */\n"
            "    left: 5px; /* Ajuste horizontal */\n"
            "    top: -5px; /* Ajuste vertical */\n"
            "}\n"
            ""
        )
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 20, 101, 31))
        font3 = QFont()
        font3.setFamilies(["Segoe UI"])
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet("")
        self.ponto_0_fuga = QLineEdit(self.groupBox_4)
        self.ponto_0_fuga.setObjectName("ponto_0_fuga")
        self.ponto_0_fuga.setGeometry(QRect(120, 20, 121, 31))
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 70, 61, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet("")
        self.ponto_x = QLineEdit(self.groupBox_4)
        self.ponto_x.setObjectName("ponto_x")
        self.ponto_x.setGeometry(QRect(80, 70, 41, 31))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(130, 70, 31, 31))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet("")
        self.ponto_x_fuga = QLineEdit(self.groupBox_4)
        self.ponto_x_fuga.setObjectName("ponto_x_fuga")
        self.ponto_x_fuga.setGeometry(QRect(170, 70, 121, 31))
        self.mostrar_valores = QPushButton(Dialog)
        self.mostrar_valores.setObjectName("mostrar_valores")
        self.mostrar_valores.setGeometry(QRect(10, 440, 121, 31))
        font4 = QFont()
        font4.setFamilies(["Segoe UI"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.mostrar_valores.setFont(font4)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "RESULTADOS NUMÉRICOS 1 GRUPO", None)
        )
        self.fundo.setText("")
        self.groupBox.setTitle(
            QCoreApplication.translate("Dialog", "Fluxos Escalares", None)
        )
        ___qtablewidgetitem = self.fluxos_escalares.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Dialog", "Fluxos", None)
        )
        ___qtablewidgetitem1 = self.fluxos_escalares.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Dialog", "X (cm)", None)
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "An\u00e1lise Espectral", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate(
                "Dialog", "Taxa de Absor\u00e7\u00e3o por Regi\u00e3o", None
            )
        )
        ___qtablewidgetitem2 = self.absorcao.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", "1", None))
        ___qtablewidgetitem3 = self.absorcao.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("Dialog", "Taxas", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("Dialog", "Fluxos Angulares", None)
        )
        ___qtablewidgetitem4 = self.fluxos_angulares.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", "1", None))
        ___qtablewidgetitem5 = self.fluxos_angulares.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", "2", None))
        ___qtablewidgetitem6 = self.fluxos_angulares.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", "3", None))
        ___qtablewidgetitem7 = self.fluxos_angulares.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", "4", None))
        self.groupBox_4.setTitle(
            QCoreApplication.translate("Dialog", "Taxa de Fuga", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Dialog",
                '<html><head/><body><p><span style=" font-size:10pt;">No ponto 0 cm = </span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog",
                '<html><head/><body><p><span style=" font-size:10pt;">No ponto</span></p></body></html>',
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "Dialog",
                '<html><head/><body><p><span style=" font-size:10pt;">cm =</span></p></body></html>',
                None,
            )
        )
        self.mostrar_valores.setText(
            QCoreApplication.translate("Dialog", "Mostrar Valores", None)
        )

    # retranslateUi
