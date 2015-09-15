# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Herevea.ui'
#
# Created: Mon Sep 14 20:57:19 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Herevea(object):
    def setupUi(self, Herevea):
        Herevea.setObjectName(_fromUtf8("Herevea"))
        Herevea.resize(787, 429)
        self.buttonBox = QtGui.QDialogButtonBox(Herevea)
        self.buttonBox.setGeometry(QtCore.QRect(420, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Herevea)
        self.label.setGeometry(QtCore.QRect(40, 50, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Herevea)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 391, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/Herevea.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Herevea)
        self.label_3.setGeometry(QtCore.QRect(190, 220, 131, 41))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/FEDER.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Herevea)
        self.label_4.setGeometry(QtCore.QRect(340, 220, 151, 41))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("img/logoConsejeria.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Herevea)
        self.label_5.setGeometry(QtCore.QRect(510, 220, 91, 41))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("img/LogoAndalucia.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Herevea)
        self.label_6.setGeometry(QtCore.QRect(30, 300, 451, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Herevea)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Herevea.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Herevea.reject)
        QtCore.QMetaObject.connectSlotsByName(Herevea)

    def retranslateUi(self, Herevea):
        Herevea.setWindowTitle(_translate("Herevea", "Herevea", None))
        self.label.setText(_translate("Herevea", "Bienvenido a Herevea!\n"
"\n"
"", None))
        self.label_6.setText(_translate("Herevea", "Seleccione una parcela catastral para comenzar su análisis", None))

