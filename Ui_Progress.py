# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\repositories\qgisplugins\herevea\Ui_Progress.ui'
#
# Created: Thu Aug 27 18:24:35 2015
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

class Ui_Progress(object):
    def setupUi(self, Progress):
        Progress.setObjectName(_fromUtf8("Progress"))
        Progress.resize(510, 107)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Progress.setWindowIcon(icon)
        self.progressBar = QtGui.QProgressBar(Progress)
        self.progressBar.setGeometry(QtCore.QRect(40, 50, 471, 21))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(Progress)
        self.label.setGeometry(QtCore.QRect(40, 20, 421, 19))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Progress)
        QtCore.QMetaObject.connectSlotsByName(Progress)

    def retranslateUi(self, Progress):
        Progress.setWindowTitle(_translate("Progress", "Herevea", None))
        self.label.setText(_translate("Progress", "Cargando...", None))

