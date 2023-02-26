# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hashgen.ui'
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


class Ui_hash(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(973, 657)
        font = QFont()
        font.setBold(True)
        Form.setFont(font)
        self.md5pushbutton = QPushButton(Form)
        self.md5pushbutton.setObjectName(u"md5pushbutton")
        self.md5pushbutton.setGeometry(QRect(820, 230, 141, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.md5pushbutton.setFont(font1)
        self.md5labe = QLabel(Form)
        self.md5labe.setObjectName(u"md5labe")
        self.md5labe.setGeometry(QRect(10, 230, 121, 51))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.md5labe.setFont(font2)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(150, 310, 651, 51))
        self.textBrowser.setFont(font1)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 230, 651, 51))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.lineEdit.setFont(font3)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 320, 111, 41))
        self.label.setFont(font2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 60, 261, 81))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        self.label_2.setFont(font4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.md5pushbutton.setText(QCoreApplication.translate("Form", u"Encode", None))
        self.md5labe.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label.setText(QCoreApplication.translate("Form", u"Hash", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Hash Generator", None))
    # retranslateUi
