# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Error.ui'
#
# Created: Wed Sep 16 00:43:02 2015
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

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName(_fromUtf8("Error"))
        Error.resize(632, 176)
        self.buttonBox = QtGui.QDialogButtonBox(Error)
        self.buttonBox.setGeometry(QtCore.QRect(250, 120, 131, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Error)
        self.label.setGeometry(QtCore.QRect(110, 30, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.image = QtGui.QLabel(Error)
        self.image.setGeometry(QtCore.QRect(20, 25, 61, 71))
        self.image.setScaledContents(True)
        self.image.setObjectName(_fromUtf8("image"))

        self.retranslateUi(Error)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Error.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Error.reject)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        Error.setWindowTitle(_translate("Error", "Error", None))
        self.image.setText(_translate("Error", "TextLabel", None))

