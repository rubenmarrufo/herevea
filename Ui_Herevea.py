# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Herevea.ui'
#
# Created: Wed Jun 17 01:05:57 2015
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
        Herevea.resize(561, 184)
        self.buttonBox = QtGui.QDialogButtonBox(Herevea)
        self.buttonBox.setGeometry(QtCore.QRect(100, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Herevea)
        self.label.setGeometry(QtCore.QRect(30, 10, 521, 101))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Herevea)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Herevea.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Herevea.reject)
        QtCore.QMetaObject.connectSlotsByName(Herevea)

    def retranslateUi(self, Herevea):
        Herevea.setWindowTitle(_translate("Herevea", "Herevea", None))
        self.label.setText(_translate("Herevea", "Bienvenido a Herevea!\n"
"\n"
"Seleccione una parcela catastral para comenzar su análisis", None))

