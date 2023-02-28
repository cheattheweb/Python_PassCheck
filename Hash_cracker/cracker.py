# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cracker.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Cracker(object):
    def setupUi(self, Cracker):
        if not Cracker.objectName():
            Cracker.setObjectName(u"Cracker")
        Cracker.resize(927, 644)
        self.hedding = QLabel(Cracker)
        self.hedding.setObjectName(u"hedding")
        self.hedding.setGeometry(QRect(350, 40, 201, 91))
        font = QFont()
        font.setPointSize(20)
        self.hedding.setFont(font)
        self.hash_labe = QLabel(Cracker)
        self.hash_labe.setObjectName(u"hash_labe")
        self.hash_labe.setGeometry(QRect(50, 180, 81, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.hash_labe.setFont(font1)
        self.hash = QLineEdit(Cracker)
        self.hash.setObjectName(u"hash")
        self.hash.setGeometry(QRect(180, 175, 551, 51))
        font2 = QFont()
        font2.setPointSize(14)
        self.hash.setFont(font2)
        self.textBrowser = QTextBrowser(Cracker)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(170, 370, 561, 51))
        self.textBrowser.setFont(font2)
        self.comboBox = QComboBox(Cracker)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 260, 171, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.comboBox.setFont(font3)
        self.crack_button = QPushButton(Cracker)
        self.crack_button.setObjectName(u"crack_button")
        self.crack_button.setGeometry(QRect(520, 260, 141, 41))
        self.crack_button.setFont(font2)
        self.status_label = QLabel(Cracker)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(180, 330, 201, 31))

        self.retranslateUi(Cracker)

        QMetaObject.connectSlotsByName(Cracker)
    # setupUi

    def retranslateUi(self, Cracker):
        Cracker.setWindowTitle(QCoreApplication.translate("Cracker", u"Form", None))
        self.hedding.setText(QCoreApplication.translate("Cracker", u"Hash Cracker", None))
        self.hash_labe.setText(QCoreApplication.translate("Cracker", u"Hash", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Cracker", u"wordlist", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Cracker", u"8 digit", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Cracker", u"7 digit", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Cracker", u"6 digit", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Cracker", u"5 digit", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Cracker", u"4 digit", None))

        self.crack_button.setText(QCoreApplication.translate("Cracker", u"Crack", None))
        self.status_label.setText("")
    # retranslateUi

