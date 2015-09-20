# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AcercaDe.ui'
#
# Created: Sat Sep 19 12:01:51 2015
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
        self.herevea = QtGui.QLabel(self.frame)
        self.herevea.setGeometry(QtCore.QRect(30, 10, 421, 131))
        self.herevea.setText(_fromUtf8(""))
        self.herevea.setPixmap(QtGui.QPixmap(_fromUtf8("img/Herevea.png")))
        self.herevea.setScaledContents(True)
        self.herevea.setObjectName(_fromUtf8("herevea"))
        self.us = QtGui.QLabel(self.frame)
        self.us.setGeometry(QtCore.QRect(320, 218, 71, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.us.sizePolicy().hasHeightForWidth())
        self.us.setSizePolicy(sizePolicy)
        self.us.setFrameShape(QtGui.QFrame.NoFrame)
        self.us.setText(_fromUtf8(""))
        self.us.setPixmap(QtGui.QPixmap(_fromUtf8("img/us.png")))
        self.us.setScaledContents(True)
        self.us.setWordWrap(True)
        self.us.setObjectName(_fromUtf8("us"))
        self.consejeria = QtGui.QLabel(self.frame)
        self.consejeria.setGeometry(QtCore.QRect(60, 218, 211, 61))
        self.consejeria.setText(_fromUtf8(""))
        self.consejeria.setPixmap(QtGui.QPixmap(_fromUtf8("img/logoConsejeria.png")))
        self.consejeria.setScaledContents(True)
        self.consejeria.setObjectName(_fromUtf8("consejeria"))
        self.feder = QtGui.QLabel(self.frame)
        self.feder.setGeometry(QtCore.QRect(70, 148, 171, 51))
        self.feder.setText(_fromUtf8(""))
        self.feder.setPixmap(QtGui.QPixmap(_fromUtf8("img/FEDER.png")))
        self.feder.setScaledContents(True)
        self.feder.setObjectName(_fromUtf8("feder"))
        self.andalucia = QtGui.QLabel(self.frame)
        self.andalucia.setGeometry(QtCore.QRect(290, 148, 121, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.andalucia.sizePolicy().hasHeightForWidth())
        self.andalucia.setSizePolicy(sizePolicy)
        self.andalucia.setFrameShape(QtGui.QFrame.NoFrame)
        self.andalucia.setText(_fromUtf8(""))
        self.andalucia.setPixmap(QtGui.QPixmap(_fromUtf8("img/LogoAndalucia.png")))
        self.andalucia.setScaledContents(True)
        self.andalucia.setWordWrap(True)
        self.andalucia.setObjectName(_fromUtf8("andalucia"))

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

