# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Herevea.ui'
#
# Created: Fri Sep 25 21:26:58 2015
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
        Herevea.setWindowModality(QtCore.Qt.WindowModal)
        Herevea.resize(509, 431)
        Herevea.setMinimumSize(QtCore.QSize(509, 431))
        Herevea.setMaximumSize(QtCore.QSize(509, 431))
        Herevea.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Herevea)
        self.buttonBox.setGeometry(QtCore.QRect(100, 370, 381, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Herevea)
        self.label.setGeometry(QtCore.QRect(30, 30, 401, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Herevea)
        self.label_2.setGeometry(QtCore.QRect(23, 80, 461, 251))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/all.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Herevea)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Herevea.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Herevea.reject)
        QtCore.QMetaObject.connectSlotsByName(Herevea)

    def retranslateUi(self, Herevea):
        Herevea.setWindowTitle(_translate("Herevea", "Herevea", None))
        self.label.setText(_translate("Herevea", "Bienvenido al programa HEREVEA...", None))

