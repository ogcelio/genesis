# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Propriedades_Fisico_Materiais_1GRYGsbw.ui'
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
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_Propriedades1G(object):
    def setupUi(self, Propriedades1G):
        if not Propriedades1G.objectName():
            Propriedades1G.setObjectName("Propriedades1G")
        Propriedades1G.resize(721, 424)
        self.fundo = QLabel(Propriedades1G)
        self.fundo.setObjectName("fundo")
        self.fundo.setGeometry(QRect(-140, -50, 1181, 651))
        self.fundo.setStyleSheet("background-color: rgb(205, 232, 210);")
        self.pushButton = QPushButton(Propriedades1G)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(30, 360, 101, 41))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.tabela_valores = QTableWidget(Propriedades1G)
        if self.tabela_valores.columnCount() < 6:
            self.tabela_valores.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_valores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if self.tabela_valores.rowCount() < 10:
            self.tabela_valores.setRowCount(10)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabela_valores.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabela_valores.setItem(0, 5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabela_valores.setItem(1, 5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabela_valores.setItem(2, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabela_valores.setItem(3, 5, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabela_valores.setItem(4, 5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tabela_valores.setItem(5, 5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tabela_valores.setItem(6, 5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tabela_valores.setItem(7, 5, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 4, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tabela_valores.setItem(8, 5, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tabela_valores.setItem(9, 5, __qtablewidgetitem75)
        self.tabela_valores.setObjectName("tabela_valores")
        self.tabela_valores.setGeometry(QRect(30, 20, 661, 331))

        self.retranslateUi(Propriedades1G)

        QMetaObject.connectSlotsByName(Propriedades1G)

    # setupUi

    def retranslateUi(self, Propriedades1G):
        Propriedades1G.setWindowTitle(
            QCoreApplication.translate("Propriedades1G", "PROPRIEDADES 1 GRUPO", None)
        )
        self.fundo.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("Propriedades1G", "Aplicar", None)
        )
        ___qtablewidgetitem = self.tabela_valores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Propriedades1G", "Sigma T", None)
        )
        ___qtablewidgetitem1 = self.tabela_valores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Propriedades1G", "Sigma S0", None)
        )
        ___qtablewidgetitem2 = self.tabela_valores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("Propriedades1G", "Sigma S1", None)
        )
        ___qtablewidgetitem3 = self.tabela_valores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("Propriedades1G", "Sigma S2", None)
        )
        ___qtablewidgetitem4 = self.tabela_valores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("Propriedades1G", "Fonte", None)
        )
        ___qtablewidgetitem5 = self.tabela_valores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("Propriedades1G", "Ni*SigmaF", None)
        )
        ___qtablewidgetitem6 = self.tabela_valores.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 1", None)
        )
        ___qtablewidgetitem7 = self.tabela_valores.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 2", None)
        )
        ___qtablewidgetitem8 = self.tabela_valores.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 3", None)
        )
        ___qtablewidgetitem9 = self.tabela_valores.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 4", None)
        )
        ___qtablewidgetitem10 = self.tabela_valores.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 5", None)
        )
        ___qtablewidgetitem11 = self.tabela_valores.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 6", None)
        )
        ___qtablewidgetitem12 = self.tabela_valores.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 7", None)
        )
        ___qtablewidgetitem13 = self.tabela_valores.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 8", None)
        )
        ___qtablewidgetitem14 = self.tabela_valores.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 9", None)
        )
        ___qtablewidgetitem15 = self.tabela_valores.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("Propriedades1G", "Zona 10", None)
        )

        __sortingEnabled = self.tabela_valores.isSortingEnabled()
        self.tabela_valores.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.tabela_valores.item(0, 0)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem17 = self.tabela_valores.item(0, 1)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("Propriedades1G", "0.9500", None)
        )
        ___qtablewidgetitem18 = self.tabela_valores.item(0, 2)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem19 = self.tabela_valores.item(0, 3)
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem20 = self.tabela_valores.item(0, 4)
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem21 = self.tabela_valores.item(0, 5)
        ___qtablewidgetitem21.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem22 = self.tabela_valores.item(1, 0)
        ___qtablewidgetitem22.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem23 = self.tabela_valores.item(1, 1)
        ___qtablewidgetitem23.setText(
            QCoreApplication.translate("Propriedades1G", "0.9300", None)
        )
        ___qtablewidgetitem24 = self.tabela_valores.item(1, 2)
        ___qtablewidgetitem24.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem25 = self.tabela_valores.item(1, 3)
        ___qtablewidgetitem25.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem26 = self.tabela_valores.item(1, 4)
        ___qtablewidgetitem26.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem27 = self.tabela_valores.item(1, 5)
        ___qtablewidgetitem27.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem28 = self.tabela_valores.item(2, 0)
        ___qtablewidgetitem28.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem29 = self.tabela_valores.item(2, 1)
        ___qtablewidgetitem29.setText(
            QCoreApplication.translate("Propriedades1G", "0.9800", None)
        )
        ___qtablewidgetitem30 = self.tabela_valores.item(2, 2)
        ___qtablewidgetitem30.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem31 = self.tabela_valores.item(2, 3)
        ___qtablewidgetitem31.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem32 = self.tabela_valores.item(2, 4)
        ___qtablewidgetitem32.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem33 = self.tabela_valores.item(2, 5)
        ___qtablewidgetitem33.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem34 = self.tabela_valores.item(3, 0)
        ___qtablewidgetitem34.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem35 = self.tabela_valores.item(3, 1)
        ___qtablewidgetitem35.setText(
            QCoreApplication.translate("Propriedades1G", "0.9200", None)
        )
        ___qtablewidgetitem36 = self.tabela_valores.item(3, 2)
        ___qtablewidgetitem36.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem37 = self.tabela_valores.item(3, 3)
        ___qtablewidgetitem37.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem38 = self.tabela_valores.item(3, 4)
        ___qtablewidgetitem38.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem39 = self.tabela_valores.item(3, 5)
        ___qtablewidgetitem39.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem40 = self.tabela_valores.item(4, 0)
        ___qtablewidgetitem40.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem41 = self.tabela_valores.item(4, 1)
        ___qtablewidgetitem41.setText(
            QCoreApplication.translate("Propriedades1G", "0.9100", None)
        )
        ___qtablewidgetitem42 = self.tabela_valores.item(4, 2)
        ___qtablewidgetitem42.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem43 = self.tabela_valores.item(4, 3)
        ___qtablewidgetitem43.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem44 = self.tabela_valores.item(4, 4)
        ___qtablewidgetitem44.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem45 = self.tabela_valores.item(4, 5)
        ___qtablewidgetitem45.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem46 = self.tabela_valores.item(5, 0)
        ___qtablewidgetitem46.setText(
            QCoreApplication.translate("Propriedades1G", "1", None)
        )
        ___qtablewidgetitem47 = self.tabela_valores.item(5, 1)
        ___qtablewidgetitem47.setText(
            QCoreApplication.translate("Propriedades1G", "0.8500", None)
        )
        ___qtablewidgetitem48 = self.tabela_valores.item(5, 2)
        ___qtablewidgetitem48.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem49 = self.tabela_valores.item(5, 3)
        ___qtablewidgetitem49.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem50 = self.tabela_valores.item(5, 4)
        ___qtablewidgetitem50.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem51 = self.tabela_valores.item(5, 5)
        ___qtablewidgetitem51.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem52 = self.tabela_valores.item(6, 0)
        ___qtablewidgetitem52.setText(
            QCoreApplication.translate("Propriedades1G", "0.2500", None)
        )
        ___qtablewidgetitem53 = self.tabela_valores.item(6, 1)
        ___qtablewidgetitem53.setText(
            QCoreApplication.translate("Propriedades1G", "0.0500", None)
        )
        ___qtablewidgetitem54 = self.tabela_valores.item(6, 2)
        ___qtablewidgetitem54.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem55 = self.tabela_valores.item(6, 3)
        ___qtablewidgetitem55.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem56 = self.tabela_valores.item(6, 4)
        ___qtablewidgetitem56.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem57 = self.tabela_valores.item(6, 5)
        ___qtablewidgetitem57.setText(
            QCoreApplication.translate("Propriedades1G", "0.2200", None)
        )
        ___qtablewidgetitem58 = self.tabela_valores.item(7, 0)
        ___qtablewidgetitem58.setText(
            QCoreApplication.translate("Propriedades1G", "0.3333", None)
        )
        ___qtablewidgetitem59 = self.tabela_valores.item(7, 1)
        ___qtablewidgetitem59.setText(
            QCoreApplication.translate("Propriedades1G", "0.2333", None)
        )
        ___qtablewidgetitem60 = self.tabela_valores.item(7, 2)
        ___qtablewidgetitem60.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem61 = self.tabela_valores.item(7, 3)
        ___qtablewidgetitem61.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem62 = self.tabela_valores.item(7, 4)
        ___qtablewidgetitem62.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem63 = self.tabela_valores.item(7, 5)
        ___qtablewidgetitem63.setText(
            QCoreApplication.translate("Propriedades1G", "0.3243", None)
        )
        ___qtablewidgetitem64 = self.tabela_valores.item(8, 0)
        ___qtablewidgetitem64.setText(
            QCoreApplication.translate("Propriedades1G", "0.2777", None)
        )
        ___qtablewidgetitem65 = self.tabela_valores.item(8, 1)
        ___qtablewidgetitem65.setText(
            QCoreApplication.translate("Propriedades1G", "0.1777", None)
        )
        ___qtablewidgetitem66 = self.tabela_valores.item(8, 2)
        ___qtablewidgetitem66.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem67 = self.tabela_valores.item(8, 3)
        ___qtablewidgetitem67.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem68 = self.tabela_valores.item(8, 4)
        ___qtablewidgetitem68.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem69 = self.tabela_valores.item(8, 5)
        ___qtablewidgetitem69.setText(
            QCoreApplication.translate("Propriedades1G", "0.2042", None)
        )
        ___qtablewidgetitem70 = self.tabela_valores.item(9, 0)
        ___qtablewidgetitem70.setText(
            QCoreApplication.translate("Propriedades1G", "0.3333", None)
        )
        ___qtablewidgetitem71 = self.tabela_valores.item(9, 1)
        ___qtablewidgetitem71.setText(
            QCoreApplication.translate("Propriedades1G", "0.2333", None)
        )
        ___qtablewidgetitem72 = self.tabela_valores.item(9, 2)
        ___qtablewidgetitem72.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem73 = self.tabela_valores.item(9, 3)
        ___qtablewidgetitem73.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem74 = self.tabela_valores.item(9, 4)
        ___qtablewidgetitem74.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        ___qtablewidgetitem75 = self.tabela_valores.item(9, 5)
        ___qtablewidgetitem75.setText(
            QCoreApplication.translate("Propriedades1G", "0", None)
        )
        self.tabela_valores.setSortingEnabled(__sortingEnabled)

    # retranslateUi
