# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_Herevea.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Herevea(object):
    def setupUi(self, Herevea):
        Herevea.setObjectName("Herevea")
        Herevea.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Herevea)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Herevea)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Herevea.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Herevea.reject)
        QtCore.QMetaObject.connectSlotsByName(Herevea)

    def retranslateUi(self, Herevea):
        Herevea.setWindowTitle(QtGui.QApplication.translate("Herevea", "Herevea", None, QtGui.QApplication.UnicodeUTF8))
