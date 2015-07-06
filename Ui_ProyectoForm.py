# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Repositories\QGisPlugins\Herevea\Ui_ProyectoForm.ui'
#
# Created: Sun Jun 21 10:28:24 2015
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

class Ui_ProyectoForm(object):
    def setupUi(self, ProyectoForm, direccion, numcatastro, superficie):
        ProyectoForm.setObjectName(_fromUtf8("ProyectoForm"))
        ProyectoForm.resize(872, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProyectoForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ProyectoForm)
        self.buttonBox.setGeometry(QtCore.QRect(510, 460, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_31 = QtGui.QLabel(ProyectoForm)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbxDireccion = QtGui.QLineEdit(ProyectoForm)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 391, 25))
        self.tbxDireccion.setReadOnly(True)
        self.tbxDireccion.setObjectName(_fromUtf8("tbxDireccion"))
        self.tbxRefCatastral = QtGui.QLineEdit(ProyectoForm)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(640, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(ProyectoForm)
        self.label_32.setGeometry(QtCore.QRect(533, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.groupBox = QtGui.QGroupBox(ProyectoForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 831, 351))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(230, 290, 231, 25))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(369, 146, 119, 23))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(29, 244, 141, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tbxSuperficie = QtGui.QDoubleSpinBox(self.groupBox)
        self.tbxSuperficie.setGeometry(QtCore.QRect(229, 96, 171, 25))
        self.tbxSuperficie.setObjectName(_fromUtf8("tbxSuperficie"))
        self.tbxSuperficie.setMaximum(100000)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(29, 196, 141, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(29, 46, 181, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(229, 146, 119, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(29, 292, 141, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(229, 196, 231, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(229, 243, 231, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(29, 146, 181, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(229, 46, 45, 25))
        self.spinBox.setMaximum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(29, 96, 181, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.tbxSuperficie.setValue(superficie)
        self.tbxDireccion.setText(direccion)
        self.tbxRefCatastral.setText(numcatastro)

        self.retranslateUi(ProyectoForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProyectoForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProyectoForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ProyectoForm)

    def retranslateUi(self, ProyectoForm):
        ProyectoForm.setWindowTitle(_translate("ProyectoForm", "Herevea", None))
        self.label_31.setText(_translate("ProyectoForm", "Direccion", None))
        self.label_32.setText(_translate("ProyectoForm", "Ref. Catastral", None))
        self.groupBox.setTitle(_translate("ProyectoForm", "Selección de proyecto", None))
        self.comboBox_3.setItemText(0, _translate("ProyectoForm", "Horizontal", None))
        self.comboBox_3.setItemText(1, _translate("ProyectoForm", "Inclinada", None))
        self.radioButton_2.setText(_translate("ProyectoForm", "Locales", None))
        self.label_5.setText(_translate("ProyectoForm", "Estructura", None))
        self.label_4.setText(_translate("ProyectoForm", "Cimentación", None))
        self.label.setText(_translate("ProyectoForm", "Nº plantas bajo rasante", None))
        self.radioButton.setText(_translate("ProyectoForm", "Viviendas", None))
        self.label_6.setText(_translate("ProyectoForm", "Cubierta", None))
        self.comboBox.setItemText(0, _translate("ProyectoForm", "Losa armada", None))
        self.comboBox.setItemText(1, _translate("ProyectoForm", "Zapatas aisladas", None))
        self.comboBox.setItemText(2, _translate("ProyectoForm", "Pilotes", None))
        self.comboBox_2.setItemText(0, _translate("ProyectoForm", "Hormigón armado", None))
        self.label_3.setText(_translate("ProyectoForm", "Planta baja", None))
        self.label_2.setText(_translate("ProyectoForm", "Superficie construida", None))

