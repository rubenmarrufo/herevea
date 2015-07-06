# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Repositories\QGisPlugins\Herevea\Ui_InmueblesList.ui'
#
# Created: Mon Jun 29 20:44:26 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from InmmueblesListTableModel import InmmueblesListTableModel

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

class Ui_InmueblesList(object):
    def setupUi(self, ProyectoForm, inmueblesList, numcatastro):
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
        self.tbxRefCatastral = QtGui.QLineEdit(ProyectoForm)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(130, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(ProyectoForm)
        self.label_32.setGeometry(QtCore.QRect(23, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.groupBox = QtGui.QGroupBox(ProyectoForm)
        self.groupBox.setGeometry(QtCore.QRect(19, 69, 831, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableInmuebles = QtGui.QTableView(self.groupBox)
        self.tableInmuebles.setGeometry(QtCore.QRect(15, 41, 801, 311))
        self.tableInmuebles.setObjectName(_fromUtf8("tableInmuebles"))
        
        self.tbxRefCatastral.setText(numcatastro)
        header = ['Ref Catastral', 'Direccion']
        tablemodel = InmueblesListTableModel(inmueblesList, header, self)
        self.tableInmuebles.setModel(tablemodel)        

        self.retranslateUi(ProyectoForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProyectoForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProyectoForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ProyectoForm)

    def retranslateUi(self, ProyectoForm):
        ProyectoForm.setWindowTitle(_translate("ProyectoForm", "Herevea", None))
        self.label_32.setText(_translate("ProyectoForm", "Ref. Catastral", None))
        self.groupBox.setTitle(_translate("ProyectoForm", "Selección de inmueble", None))

