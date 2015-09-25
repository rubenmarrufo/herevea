# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AcercaDe.ui'
#
# Created: Fri Sep 25 21:27:22 2015
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

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName(_fromUtf8("AcercaDe"))
        AcercaDe.setWindowModality(QtCore.Qt.WindowModal)
        AcercaDe.resize(825, 381)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AcercaDe.sizePolicy().hasHeightForWidth())
        AcercaDe.setSizePolicy(sizePolicy)
        AcercaDe.setMinimumSize(QtCore.QSize(825, 381))
        AcercaDe.setMaximumSize(QtCore.QSize(825, 381))
        self.buttonBox = QtGui.QDialogButtonBox(AcercaDe)
        self.buttonBox.setGeometry(QtCore.QRect(420, 320, 381, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(AcercaDe)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 359, 271))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.frame = QtGui.QFrame(AcercaDe)
        self.frame.setGeometry(QtCore.QRect(360, 0, 471, 301))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(27, 30, 421, 241))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/all.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(AcercaDe)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AcercaDe.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AcercaDe.reject)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        AcercaDe.setWindowTitle(_translate("AcercaDe", "Herevea", None))
        self.label.setText(_translate("AcercaDe", "HEREVEA ha sido desarrollado por:", None))
        self.label_6.setText(_translate("AcercaDe", "Investigador Principal:\n"
"Madelyn Marrero Meléndez.\n"
"\n"
"Investigadores:\n"
"Jaime Solís Guzmán\n"
"Rafael Llácer Pantión\n"
"Rafael Lucas Ruiz\n"
"Antonio Ramírez de Arellano Agudo\n"
"Alejandro Martínez Rocamora\n"
"Mª Desirée Alba Rodríguez\n"
"Patricia González Vallejo\n"
"Rocío Ruíz Pérez", None))

