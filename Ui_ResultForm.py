# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ResultForm.ui'
#
# Created: Mon Sep 14 22:29:40 2015
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

class Ui_ResultForm(object):
    def setupUi(self, ResultForm):
        ResultForm.setObjectName(_fromUtf8("ResultForm"))
        ResultForm.resize(1165, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ResultForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ResultForm)
        self.buttonBox.setGeometry(QtCore.QRect(773, 690, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tbxDireccion = QtGui.QLineEdit(ResultForm)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 561, 25))
        self.tbxDireccion.setReadOnly(True)
        self.tbxDireccion.setObjectName(_fromUtf8("tbxDireccion"))
        self.label_32 = QtGui.QLabel(ResultForm)
        self.label_32.setGeometry(QtCore.QRect(700, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.tbxRefCatastral = QtGui.QLineEdit(ResultForm)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(807, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_31 = QtGui.QLabel(ResultForm)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tabWidget = QtGui.QTabWidget(ResultForm)
        self.tabWidget.setGeometry(QtCore.QRect(13, 70, 1141, 601))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabHERehParcial = QtGui.QTableWidget(self.tab)
        self.tabHERehParcial.setGeometry(QtCore.QRect(20, 70, 1101, 141))
        self.tabHERehParcial.setObjectName(_fromUtf8("tabHERehParcial"))
        self.tabHERehParcial.setColumnCount(6)
        self.tabHERehParcial.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehParcial.setHorizontalHeaderItem(5, item)
        self.tabHERehParcial.horizontalHeader().setDefaultSectionSize(151)
        self.tabHERehParcial.horizontalHeader().setMinimumSectionSize(59)
        self.tabHERehParcial.verticalHeader().setDefaultSectionSize(46)
        self.tabHERehTotal = QtGui.QTableWidget(self.tab)
        self.tabHERehTotal.setGeometry(QtCore.QRect(340, 240, 491, 141))
        self.tabHERehTotal.setObjectName(_fromUtf8("tabHERehTotal"))
        self.tabHERehTotal.setColumnCount(1)
        self.tabHERehTotal.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHERehTotal.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehTotal.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHERehTotal.setHorizontalHeaderItem(0, item)
        self.tabHERehTotal.horizontalHeader().setDefaultSectionSize(310)
        self.tabHERehTotal.verticalHeader().setDefaultSectionSize(46)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 6, 1111, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tabHEDemParcial = QtGui.QTableWidget(self.groupBox)
        self.tabHEDemParcial.setGeometry(QtCore.QRect(10, 30, 1091, 111))
        self.tabHEDemParcial.setObjectName(_fromUtf8("tabHEDemParcial"))
        self.tabHEDemParcial.setColumnCount(6)
        self.tabHEDemParcial.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemParcial.setHorizontalHeaderItem(5, item)
        self.tabHEDemParcial.horizontalHeader().setDefaultSectionSize(150)
        self.tabHEDemParcial.horizontalHeader().setMinimumSectionSize(57)
        self.tabHEDemParcial.verticalHeader().setDefaultSectionSize(34)
        self.tabHEDemTotal = QtGui.QTableWidget(self.groupBox)
        self.tabHEDemTotal.setGeometry(QtCore.QRect(350, 150, 481, 111))
        self.tabHEDemTotal.setObjectName(_fromUtf8("tabHEDemTotal"))
        self.tabHEDemTotal.setColumnCount(1)
        self.tabHEDemTotal.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemTotal.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemTotal.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEDemTotal.setHorizontalHeaderItem(0, item)
        self.tabHEDemTotal.horizontalHeader().setDefaultSectionSize(307)
        self.tabHEDemTotal.horizontalHeader().setMinimumSectionSize(46)
        self.tabHEDemTotal.verticalHeader().setDefaultSectionSize(34)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 1111, 271))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tabHEConsParcial = QtGui.QTableWidget(self.groupBox_2)
        self.tabHEConsParcial.setGeometry(QtCore.QRect(10, 30, 1091, 111))
        self.tabHEConsParcial.setObjectName(_fromUtf8("tabHEConsParcial"))
        self.tabHEConsParcial.setColumnCount(6)
        self.tabHEConsParcial.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsParcial.setHorizontalHeaderItem(5, item)
        self.tabHEConsParcial.horizontalHeader().setDefaultSectionSize(150)
        self.tabHEConsParcial.horizontalHeader().setMinimumSectionSize(59)
        self.tabHEConsParcial.verticalHeader().setDefaultSectionSize(34)
        self.tabHEConsTotal = QtGui.QTableWidget(self.groupBox_2)
        self.tabHEConsTotal.setGeometry(QtCore.QRect(350, 150, 481, 111))
        self.tabHEConsTotal.setObjectName(_fromUtf8("tabHEConsTotal"))
        self.tabHEConsTotal.setColumnCount(1)
        self.tabHEConsTotal.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsTotal.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsTotal.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEConsTotal.setHorizontalHeaderItem(0, item)
        self.tabHEConsTotal.horizontalHeader().setDefaultSectionSize(307)
        self.tabHEConsTotal.horizontalHeader().setMinimumSectionSize(46)
        self.tabHEConsTotal.verticalHeader().setDefaultSectionSize(34)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.ComparativadeHuella = QtGui.QWidget()
        self.ComparativadeHuella.setObjectName(_fromUtf8("ComparativadeHuella"))
        self.tabHEComp = QtGui.QTableWidget(self.ComparativadeHuella)
        self.tabHEComp.setGeometry(QtCore.QRect(70, 80, 991, 131))
        self.tabHEComp.setObjectName(_fromUtf8("tabHEComp"))
        self.tabHEComp.setColumnCount(2)
        self.tabHEComp.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabHEComp.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEComp.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEComp.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabHEComp.setHorizontalHeaderItem(1, item)
        self.tabHEComp.horizontalHeader().setDefaultSectionSize(408)
        self.tabHEComp.horizontalHeader().setMinimumSectionSize(76)
        self.tabHEComp.verticalHeader().setDefaultSectionSize(44)
        self.tabWidget.addTab(self.ComparativadeHuella, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabPEMReh = QtGui.QTableWidget(self.tab_3)
        self.tabPEMReh.setGeometry(QtCore.QRect(170, 110, 801, 81))
        self.tabPEMReh.setObjectName(_fromUtf8("tabPEMReh"))
        self.tabPEMReh.setColumnCount(1)
        self.tabPEMReh.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tabPEMReh.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMReh.setHorizontalHeaderItem(0, item)
        self.tabPEMReh.horizontalHeader().setDefaultSectionSize(670)
        self.tabPEMReh.horizontalHeader().setMinimumSectionSize(230)
        self.tabPEMReh.verticalHeader().setDefaultSectionSize(40)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 290, 1091, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tabPEMCons = QtGui.QTableWidget(self.groupBox_3)
        self.tabPEMCons.setGeometry(QtCore.QRect(140, 50, 801, 131))
        self.tabPEMCons.setObjectName(_fromUtf8("tabPEMCons"))
        self.tabPEMCons.setColumnCount(1)
        self.tabPEMCons.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tabPEMCons.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMCons.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMCons.setHorizontalHeaderItem(0, item)
        self.tabPEMCons.horizontalHeader().setDefaultSectionSize(635)
        self.tabPEMCons.horizontalHeader().setMinimumSectionSize(220)
        self.tabPEMCons.verticalHeader().setDefaultSectionSize(45)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 50, 1091, 211))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tabPEMDem = QtGui.QTableWidget(self.groupBox_4)
        self.tabPEMDem.setGeometry(QtCore.QRect(140, 50, 801, 81))
        self.tabPEMDem.setObjectName(_fromUtf8("tabPEMDem"))
        self.tabPEMDem.setColumnCount(1)
        self.tabPEMDem.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tabPEMDem.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMDem.setHorizontalHeaderItem(0, item)
        self.tabPEMDem.horizontalHeader().setDefaultSectionSize(670)
        self.tabPEMDem.horizontalHeader().setMinimumSectionSize(230)
        self.tabPEMDem.verticalHeader().setDefaultSectionSize(40)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabPEMComp = QtGui.QTableWidget(self.tab_5)
        self.tabPEMComp.setGeometry(QtCore.QRect(110, 110, 941, 91))
        self.tabPEMComp.setObjectName(_fromUtf8("tabPEMComp"))
        self.tabPEMComp.setColumnCount(2)
        self.tabPEMComp.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tabPEMComp.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMComp.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPEMComp.setHorizontalHeaderItem(1, item)
        self.tabPEMComp.horizontalHeader().setDefaultSectionSize(400)
        self.tabPEMComp.horizontalHeader().setMinimumSectionSize(120)
        self.tabPEMComp.verticalHeader().setDefaultSectionSize(46)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))

        self.retranslateUi(ResultForm)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ResultForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ResultForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ResultForm)

    def retranslateUi(self, ResultForm):
        ResultForm.setWindowTitle(_translate("ResultForm", "Herevea", None))
        self.label_32.setText(_translate("ResultForm", "Ref. Catastral", None))
        self.label_31.setText(_translate("ResultForm", "Direccion", None))
        item = self.tabHERehParcial.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Parcial (hag/m2)", None))
        item = self.tabHERehParcial.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Parcial (hag)", None))
        item = self.tabHERehParcial.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Energía", None))
        item = self.tabHERehParcial.horizontalHeaderItem(1)
        item.setText(_translate("ResultForm", "Bosques", None))
        item = self.tabHERehParcial.horizontalHeaderItem(2)
        item.setText(_translate("ResultForm", "Pastos", None))
        item = self.tabHERehParcial.horizontalHeaderItem(3)
        item.setText(_translate("ResultForm", "Mar", None))
        item = self.tabHERehParcial.horizontalHeaderItem(4)
        item.setText(_translate("ResultForm", "Cultivos", None))
        item = self.tabHERehParcial.horizontalHeaderItem(5)
        item.setText(_translate("ResultForm", "Superficie cons.", None))
        item = self.tabHERehTotal.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Total (hag/m2)", None))
        item = self.tabHERehTotal.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Total (hag)", None))
        item = self.tabHERehTotal.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Total", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ResultForm", "HE rehabilitación", None))
        self.groupBox.setTitle(_translate("ResultForm", "Demolición", None))
        item = self.tabHEDemParcial.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Parcial (hag/m2)", None))
        item = self.tabHEDemParcial.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Parcial (hag)", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Energía", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(1)
        item.setText(_translate("ResultForm", "Bosques", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(2)
        item.setText(_translate("ResultForm", "Pastos", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(3)
        item.setText(_translate("ResultForm", "Mar", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(4)
        item.setText(_translate("ResultForm", "Cultivos", None))
        item = self.tabHEDemParcial.horizontalHeaderItem(5)
        item.setText(_translate("ResultForm", "Supeficie cons.", None))
        item = self.tabHEDemTotal.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Total (hag/m2)", None))
        item = self.tabHEDemTotal.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Total (hag)", None))
        item = self.tabHEDemTotal.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Total", None))
        self.groupBox_2.setTitle(_translate("ResultForm", "Nueva construcción", None))
        item = self.tabHEConsParcial.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Parcial (hag/m2)", None))
        item = self.tabHEConsParcial.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Parcial (hag)", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Energía", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(1)
        item.setText(_translate("ResultForm", "Bosques", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(2)
        item.setText(_translate("ResultForm", "Pastos", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(3)
        item.setText(_translate("ResultForm", "Mar", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(4)
        item.setText(_translate("ResultForm", "Cultivos", None))
        item = self.tabHEConsParcial.horizontalHeaderItem(5)
        item.setText(_translate("ResultForm", "Supeficie cons.", None))
        item = self.tabHEConsTotal.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Total (hag/m2)", None))
        item = self.tabHEConsTotal.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Total (hag)", None))
        item = self.tabHEConsTotal.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Total", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ResultForm", "HE demolición y construcción", None))
        item = self.tabHEComp.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "HE Total (hag/m2)", None))
        item = self.tabHEComp.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "HE Total (hag)", None))
        item = self.tabHEComp.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Rehabilitación", None))
        item = self.tabHEComp.horizontalHeaderItem(1)
        item.setText(_translate("ResultForm", "Demolición + Nueva Construcción", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ComparativadeHuella), _translate("ResultForm", "Comparativa de HE", None))
        item = self.tabPEMReh.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "PEM Total (€)", None))
        item = self.tabPEMReh.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Rehabilitación", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ResultForm", "PEM Rehabilitacion", None))
        self.groupBox_3.setTitle(_translate("ResultForm", "Nueva Construcción", None))
        item = self.tabPEMCons.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "PEM Total (€/m2)", None))
        item = self.tabPEMCons.verticalHeaderItem(1)
        item.setText(_translate("ResultForm", "PEM Total (€)", None))
        item = self.tabPEMCons.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Nueva construcción", None))
        self.groupBox_4.setTitle(_translate("ResultForm", "Demolición", None))
        item = self.tabPEMDem.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "PEM Total (€)", None))
        item = self.tabPEMDem.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Demolición", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ResultForm", "PEM demolición y construcción", None))
        item = self.tabPEMComp.verticalHeaderItem(0)
        item.setText(_translate("ResultForm", "PEM Total (€)", None))
        item = self.tabPEMComp.horizontalHeaderItem(0)
        item.setText(_translate("ResultForm", "Rehabilitación", None))
        item = self.tabPEMComp.horizontalHeaderItem(1)
        item.setText(_translate("ResultForm", "Demolición + Nueva construcción", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("ResultForm", "Comparativa de PEM", None))
