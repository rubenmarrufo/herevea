# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_UsuarioForm.ui'
#
# Created: Wed Aug 19 19:54:28 2015
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
    def setupUi(self, UsuarioForm, parcelaService):
        UsuarioForm.setObjectName(_fromUtf8("UsuarioForm"))
        UsuarioForm.resize(957, 455)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UsuarioForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(UsuarioForm)
        self.buttonBox.setGeometry(QtCore.QRect(600, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_31 = QtGui.QLabel(UsuarioForm)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbxDireccion = QtGui.QLineEdit(UsuarioForm)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 501, 25))
        self.tbxDireccion.setReadOnly(True)
        self.tbxDireccion.setObjectName(_fromUtf8("tbxDireccion"))
        self.tbxRefCatastral = QtGui.QLineEdit(UsuarioForm)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(730, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(UsuarioForm)
        self.label_32.setGeometry(QtCore.QRect(623, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.groupBox = QtGui.QGroupBox(UsuarioForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 921, 311))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 149, 141, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 53, 141, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cbCubierta = QtGui.QComboBox(self.groupBox)
        self.cbCubierta.setGeometry(QtCore.QRect(231, 147, 231, 25))
        self.cbCubierta.setObjectName(_fromUtf8("cbCubierta"))
        self.cbCubierta.addItem(_fromUtf8(""))
        self.cbCubierta.addItem(_fromUtf8(""))
        self.cbCimentacion = QtGui.QComboBox(self.groupBox)
        self.cbCimentacion.setGeometry(QtCore.QRect(230, 53, 231, 25))
        self.cbCimentacion.setObjectName(_fromUtf8("cbCimentacion"))
        self.cbCimentacion.addItem(_fromUtf8(""))
        self.cbCimentacion.addItem(_fromUtf8(""))
        self.cbCimentacion.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 101, 141, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cbEstructura = QtGui.QComboBox(self.groupBox)
        self.cbEstructura.setGeometry(QtCore.QRect(230, 100, 231, 25))
        self.cbEstructura.setObjectName(_fromUtf8("cbEstructura"))
        self.cbEstructura.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 181, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 250, 141, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 198, 101, 25))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(230, 247, 101, 25))
        self.doubleSpinBox_2.setMaximum(9999.99)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        
        self.tbxDireccion.setText(parcelaService.getDireccion())
        self.tbxRefCatastral.setText(parcelaService.getNumCatastro())
        
        self.retranslateUi(UsuarioForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UsuarioForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UsuarioForm.reject)
        QtCore.QMetaObject.connectSlotsByName(UsuarioForm)

    def retranslateUi(self, UsuarioForm):
        UsuarioForm.setWindowTitle(_translate("UsuarioForm", "Herevea", None))
        self.label_31.setText(_translate("UsuarioForm", "Direccion", None))
        self.label_32.setText(_translate("UsuarioForm", "Ref. Catastral", None))
        self.groupBox.setTitle(_translate("UsuarioForm", "Informacion usuario", None))
        self.label_6.setText(_translate("UsuarioForm", "Cubierta", None))
        self.label_4.setText(_translate("UsuarioForm", "Cimentación", None))
        self.cbCubierta.setItemText(0, _translate("UsuarioForm", "Horizontal", None))
        self.cbCubierta.setItemText(1, _translate("UsuarioForm", "Inclinada", None))
        self.cbCimentacion.setItemText(0, _translate("UsuarioForm", "Losa armada", None))
        self.cbCimentacion.setItemText(1, _translate("UsuarioForm", "Zapatas aisladas", None))
        self.cbCimentacion.setItemText(2, _translate("UsuarioForm", "Pilotes", None))
        self.label_5.setText(_translate("UsuarioForm", "Estructura", None))
        self.cbEstructura.setItemText(0, _translate("UsuarioForm", "Hormigón armada", None))
        self.label_7.setText(_translate("UsuarioForm", "Altura media por planta", None))
        self.label_8.setText(_translate("UsuarioForm", "Altura del edificio", None))

