# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SeleccionForm.ui'
#
# Created: Tue Sep 15 19:38:43 2015
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

class Ui_UsuarioForm(object):
    def setupUi(self, UsuarioForm):
        UsuarioForm.setObjectName(_fromUtf8("UsuarioForm"))
        UsuarioForm.resize(751, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UsuarioForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(UsuarioForm)
        self.buttonBox.setGeometry(QtCore.QRect(350, 458, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(UsuarioForm)
        self.label.setGeometry(QtCore.QRect(60, 20, 631, 61))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(UsuarioForm)
        self.groupBox.setGeometry(QtCore.QRect(60, 100, 631, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_33 = QtGui.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(33, 47, 181, 20))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(34, 87, 181, 20))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.cmbProvincia = QtGui.QComboBox(self.groupBox)
        self.cmbProvincia.setGeometry(QtCore.QRect(190, 45, 391, 25))
        self.cmbProvincia.setObjectName(_fromUtf8("cmbProvincia"))
        self.cmbProvincia.addItem(_fromUtf8(""))
        self.cmbMunicipio = QtGui.QComboBox(self.groupBox)
        self.cmbMunicipio.setGeometry(QtCore.QRect(190, 85, 391, 25))
        self.cmbMunicipio.setObjectName(_fromUtf8("cmbMunicipio"))
        self.cmbMunicipio.addItem(_fromUtf8(""))
        self.radCatastro = QtGui.QRadioButton(UsuarioForm)
        self.radCatastro.setGeometry(QtCore.QRect(78, 321, 371, 23))
        self.radCatastro.setObjectName(_fromUtf8("radCatastro"))
        self.radMapa = QtGui.QRadioButton(UsuarioForm)
        self.radMapa.setGeometry(QtCore.QRect(76, 270, 371, 23))
        self.radMapa.setObjectName(_fromUtf8("radMapa"))
        self.groupBox_2 = QtGui.QGroupBox(UsuarioForm)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 359, 631, 71))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tbxRefCatastral = QtGui.QLineEdit(self.groupBox_2)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(190, 24, 381, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(32, 24, 181, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))

        self.retranslateUi(UsuarioForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UsuarioForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UsuarioForm.reject)
        QtCore.QMetaObject.connectSlotsByName(UsuarioForm)

    def retranslateUi(self, UsuarioForm):
        UsuarioForm.setWindowTitle(_translate("UsuarioForm", "Herevea", None))
        self.label.setText(_translate("UsuarioForm", "Para iniciar el análisis introduza los datos catastrales de la parcela o seleccione la parcela en el mapa:", None))
        self.groupBox.setTitle(_translate("UsuarioForm", "Localización de la parcela", None))
        self.label_33.setText(_translate("UsuarioForm", "Provincia", None))
        self.label_34.setText(_translate("UsuarioForm", "Municipio", None))
        self.cmbProvincia.setItemText(0, _translate("UsuarioForm", "Sevilla", None))
        self.cmbMunicipio.setItemText(0, _translate("UsuarioForm", "Sevilla", None))
        self.radCatastro.setText(_translate("UsuarioForm", "Selección mediante información catastral", None))
        self.radMapa.setText(_translate("UsuarioForm", "Selección manual de la parcela en el mapa", None))
        self.label_32.setText(_translate("UsuarioForm", "Referencia Catastral", None))

