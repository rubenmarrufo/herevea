# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ProyectoForm.ui'
#
# Created: Wed Aug 19 19:39:57 2015
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
    def setupUi(self, ProyectoForm, parcelaService):
        ProyectoForm.setObjectName(_fromUtf8("ProyectoForm"))
        ProyectoForm.resize(872, 586)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProyectoForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ProyectoForm)
        self.buttonBox.setGeometry(QtCore.QRect(510, 530, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_31 = QtGui.QLabel(ProyectoForm)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbxDireccion = QtGui.QLineEdit(ProyectoForm)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 411, 25))
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
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 831, 441))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radOtrosUsos = QtGui.QRadioButton(self.groupBox)
        self.radOtrosUsos.setGeometry(QtCore.QRect(369, 327, 119, 23))
        self.radOtrosUsos.setObjectName(_fromUtf8("radOtrosUsos"))
        self.tbxSuperficie = QtGui.QDoubleSpinBox(self.groupBox)
        self.tbxSuperficie.setGeometry(QtCore.QRect(229, 173, 171, 25))
        self.tbxSuperficie.setObjectName(_fromUtf8("tbxSuperficie"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 222, 181, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.radViviendas = QtGui.QRadioButton(self.groupBox)
        self.radViviendas.setGeometry(QtCore.QRect(229, 327, 119, 23))
        self.radViviendas.setChecked(True)
        self.radViviendas.setObjectName(_fromUtf8("radViviendas"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 327, 181, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tbxPlantasBajoRasante = QtGui.QSpinBox(self.groupBox)
        self.tbxPlantasBajoRasante.setGeometry(QtCore.QRect(229, 222, 51, 25))
        self.tbxPlantasBajoRasante.setMaximum(10)
        self.tbxPlantasBajoRasante.setObjectName(_fromUtf8("tbxPlantasBajoRasante"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(29, 175, 181, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 37, 141, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tbxAntiguedad = QtGui.QSpinBox(self.groupBox)
        self.tbxAntiguedad.setGeometry(QtCore.QRect(230, 36, 101, 25))
        self.tbxAntiguedad.setMaximum(1)
        self.tbxAntiguedad.setObjectName(_fromUtf8("tbxAntiguedad"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 84, 141, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cbTipoInmueble = QtGui.QComboBox(self.groupBox)
        self.cbTipoInmueble.setGeometry(QtCore.QRect(230, 81, 231, 25))
        self.cbTipoInmueble.setObjectName(_fromUtf8("cbTipoInmueble"))
        self.cbTipoInmueble.addItem(_fromUtf8(""))
        self.cbTipoInmueble.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 130, 68, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tbxUso = QtGui.QLineEdit(self.groupBox)
        self.tbxUso.setGeometry(QtCore.QRect(230, 127, 231, 25))
        self.tbxUso.setReadOnly(True)
        self.tbxUso.setObjectName(_fromUtf8("tbxUso"))
        self.tbxPlantasSobreRasante = QtGui.QSpinBox(self.groupBox)
        self.tbxPlantasSobreRasante.setGeometry(QtCore.QRect(230, 275, 51, 25))
        self.tbxPlantasSobreRasante.setMaximum(100)
        self.tbxPlantasSobreRasante.setObjectName(_fromUtf8("tbxPlantasSobreRasante"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(31, 275, 181, 19))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 380, 181, 19))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tbxNInmuebles = QtGui.QSpinBox(self.groupBox)
        self.tbxNInmuebles.setGeometry(QtCore.QRect(230, 380, 51, 25))
        self.tbxNInmuebles.setMaximum(100)
        self.tbxNInmuebles.setObjectName(_fromUtf8("tbxNInmuebles"))
        
        self.tbxDireccion.setText(parcelaService.getDireccion())
        self.tbxRefCatastral.setText(parcelaService.getNumCatastro())
        self.tbxAntiguedad.setMaximum(99999)
        self.tbxAntiguedad.setValue(parcelaService.getAntiguedad())
        self.cbTipoInmueble.setCurrentIndex(0 if parcelaService.isInmuebleUnico() else 1)
        self.tbxUso.setText(parcelaService.uso())
        self.tbxSuperficie.setMaximum(9999)
        self.tbxSuperficie.setValue(parcelaService.getSuperficie())
        self.tbxPlantasBajoRasante.setValue(parcelaService.plantas()['plantasBajo'])
        self.tbxPlantasSobreRasante.setValue(parcelaService.plantas()['plantasSobre'])        
        self.radViviendas.setChecked(parcelaService.plantaBajoViviendas())
        self.radOtrosUsos.setChecked(not parcelaService.plantaBajoViviendas())

        self.retranslateUi(ProyectoForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProyectoForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProyectoForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ProyectoForm)

    def retranslateUi(self, ProyectoForm):
        ProyectoForm.setWindowTitle(_translate("ProyectoForm", "Herevea", None))
        self.label_31.setText(_translate("ProyectoForm", "Direccion", None))
        self.label_32.setText(_translate("ProyectoForm", "Ref. Catastral", None))
        self.groupBox.setTitle(_translate("ProyectoForm", "Informacion catastral", None))
        self.radOtrosUsos.setText(_translate("ProyectoForm", "Otros usos", None))
        self.label.setText(_translate("ProyectoForm", "Nº plantas bajo rasante", None))
        self.radViviendas.setText(_translate("ProyectoForm", "Viviendas", None))
        self.label_3.setText(_translate("ProyectoForm", "Planta baja", None))
        self.label_2.setText(_translate("ProyectoForm", "Superficie construida", None))
        self.label_7.setText(_translate("ProyectoForm", "Año construcción", None))
        self.label_8.setText(_translate("ProyectoForm", "Tipo de inmueble", None))
        self.cbTipoInmueble.setItemText(0, _translate("ProyectoForm", "Inmueble único", None))
        self.cbTipoInmueble.setItemText(1, _translate("ProyectoForm", "División horizontal", None))
        self.label_9.setText(_translate("ProyectoForm", "Uso", None))
        self.label_10.setText(_translate("ProyectoForm", "Nº plantas sobre rasante", None))
        self.label_11.setText(_translate("ProyectoForm", "Nº de inmuebles", None))