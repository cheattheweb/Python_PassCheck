# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QTextBrowser, QWidget)


class Ui_Widget(object):
    def setupUi(self, Ui_Widget):
        if not Ui_Widget.objectName():
            Ui_Widget.setObjectName(u"Ui_Widget")
        Ui_Widget.resize(1921, 887)
        font = QFont()
        font.setPointSize(14)
        Ui_Widget.setFont(font)
        self.UserName = QLabel(Ui_Widget)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setGeometry(QRect(60, 180, 111, 51))
        self.UserName.setFont(font)
        self.label_2 = QLabel(Ui_Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 260, 111, 41))
        self.label_2.setFont(font)
        self.pushButton = QPushButton(Ui_Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(760, 320, 231, 51))
        self.UserNameInput = QLineEdit(Ui_Widget)
        self.UserNameInput.setObjectName(u"UserNameInput")
        self.UserNameInput.setGeometry(QRect(200, 180, 851, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.UserNameInput.setFont(font1)
        self.PassInput = QLineEdit(Ui_Widget)
        self.PassInput.setObjectName(u"PassInput")
        self.PassInput.setGeometry(QRect(200, 260, 851, 41))
        self.appName = QLabel(Ui_Widget)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(820, 20, 281, 81))
        font2 = QFont()
        font2.setPointSize(30)
        self.appName.setFont(font2)
        self.description = QLabel(Ui_Widget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(640, 90, 591, 71))
        self.passInfo_2 = QLabel(Ui_Widget)
        self.passInfo_2.setObjectName(u"passInfo_2")
        self.passInfo_2.setGeometry(QRect(30, 490, 101, 41))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.passInfo_2.setFont(font3)
        self.passInfo_3 = QLabel(Ui_Widget)
        self.passInfo_3.setObjectName(u"passInfo_3")
        self.passInfo_3.setGeometry(QRect(30, 550, 101, 41))
        self.passInfo_3.setFont(font3)
        self.passInfo_4 = QLabel(Ui_Widget)
        self.passInfo_4.setObjectName(u"passInfo_4")
        self.passInfo_4.setGeometry(QRect(30, 600, 151, 41))
        self.passInfo_4.setFont(font3)
        self.passInfo_5 = QLabel(Ui_Widget)
        self.passInfo_5.setObjectName(u"passInfo_5")
        self.passInfo_5.setGeometry(QRect(30, 660, 151, 31))
        self.passInfo_5.setFont(font3)
        self.textBrowser = QTextBrowser(Ui_Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(1120, 170, 751, 681))
        self.guesses = QLabel(Ui_Widget)
        self.guesses.setObjectName(u"guesses")
        self.guesses.setGeometry(QRect(200, 500, 151, 22))
        self.tenH = QLabel(Ui_Widget)
        self.tenH.setObjectName(u"tenH")
        self.tenH.setGeometry(QRect(200, 560, 151, 22))
        self.tenKS = QLabel(Ui_Widget)
        self.tenKS.setObjectName(u"tenKS")
        self.tenKS.setGeometry(QRect(200, 610, 161, 22))
        self.tenBS = QLabel(Ui_Widget)
        self.tenBS.setObjectName(u"tenBS")
        self.tenBS.setGeometry(QRect(200, 660, 161, 22))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setUnderline(False)
        self.tenBS.setFont(font4)

        self.retranslateUi(Ui_Widget)

        QMetaObject.connectSlotsByName(Ui_Widget)

    # setupUi

    def retranslateUi(self, Ui_Widget):
        Ui_Widget.setWindowTitle(QCoreApplication.translate("Ui_Widget", u"Form", None))
        self.UserName.setText(QCoreApplication.translate("Ui_Widget", u"User Name", None))
        self.label_2.setText(QCoreApplication.translate("Ui_Widget", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Ui_Widget", u"Check The Password", None))
        self.appName.setText(QCoreApplication.translate("Ui_Widget", u"PassCheck", None))
        self.description.setText(QCoreApplication.translate("Ui_Widget",
                                                            u"<html><head/><body><p><span style=\" font-size:12pt;\">A </span><span style=\" font-size:12pt; font-weight:600;\">Free and OpenSource </span><span style=\" font-size:12pt;\">Password Strength Checker. <br/>It uses real password patterns to mesure the strenght of a given password.</span></p></body></html>",
                                                            None))
        self.passInfo_2.setText(QCoreApplication.translate("Ui_Widget", u"Guesses :", None))
        self.passInfo_3.setText(QCoreApplication.translate("Ui_Widget", u"100 / hour:", None))
        self.passInfo_4.setText(QCoreApplication.translate("Ui_Widget", u"10k / second:", None))
        self.passInfo_5.setText(QCoreApplication.translate("Ui_Widget", u"10B / second:", None))
        self.guesses.setText("")
        self.tenH.setText("")
        self.tenKS.setText("")
        self.tenBS.setText("")
    # retranslateUi
