# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ConfiguracionForm.ui'
#
# Created: Sun Nov 08 11:35:18 2015
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

class Ui_ConfiguracionForm(object):
    def setupUi(self, ConfiguracionForm):
        ConfiguracionForm.setObjectName(_fromUtf8("ConfiguracionForm"))
        ConfiguracionForm.resize(731, 196)
        ConfiguracionForm.setMinimumSize(QtCore.QSize(731, 0))
        ConfiguracionForm.setMaximumSize(QtCore.QSize(731, 920))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfiguracionForm.setWindowIcon(icon)
        self.label = QtGui.QLabel(ConfiguracionForm)
        self.label.setGeometry(QtCore.QRect(40, 20, 631, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbxPath = QtGui.QLineEdit(ConfiguracionForm)
        self.tbxPath.setGeometry(QtCore.QRect(40, 60, 641, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.tbxPath.setFont(font)
        self.tbxPath.setReadOnly(False)
        self.tbxPath.setObjectName(_fromUtf8("tbxPath"))
        self.label_2 = QtGui.QLabel(ConfiguracionForm)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 641, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(6)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(ConfiguracionForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 140, 251, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAccept = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnAccept.setObjectName(_fromUtf8("btnAccept"))
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnCancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.retranslateUi(ConfiguracionForm)
        QtCore.QMetaObject.connectSlotsByName(ConfiguracionForm)

    def retranslateUi(self, ConfiguracionForm):
        ConfiguracionForm.setWindowTitle(_translate("ConfiguracionForm", "Herevea", None))
        self.label.setText(_translate("ConfiguracionForm", "Ruta para archivos intermedios:", None))
        self.label_2.setText(_translate("ConfiguracionForm", "Herevea usa archivos intermedios para los cálculos y la generación de informes. Asegúrese de que dispone de permisos de escritura sobre esta carpeta", None))
        self.btnAccept.setText(_translate("ConfiguracionForm", "Aceptar", None))
        self.btnCancel.setText(_translate("ConfiguracionForm", "Cancelar", None))

