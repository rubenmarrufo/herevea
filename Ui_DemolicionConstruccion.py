# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DemolicionConstruccion.ui'
#
# Created: Wed Oct 28 22:30:07 2015
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

class Ui_DemolicionConstruccion(object):
    def setupUi(self, DemolicionConstruccion):
        DemolicionConstruccion.setObjectName(_fromUtf8("DemolicionConstruccion"))
        DemolicionConstruccion.resize(1037, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DemolicionConstruccion.setWindowIcon(icon)
        self.label_31 = QtGui.QLabel(DemolicionConstruccion)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbxDireccion = QtGui.QLineEdit(DemolicionConstruccion)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 561, 25))
        self.tbxDireccion.setReadOnly(True)
        self.tbxDireccion.setObjectName(_fromUtf8("tbxDireccion"))
        self.tbxRefCatastral = QtGui.QLineEdit(DemolicionConstruccion)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(807, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(DemolicionConstruccion)
        self.label_32.setGeometry(QtCore.QRect(700, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayoutWidget = QtGui.QWidget(DemolicionConstruccion)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(691, 440, 331, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.btnAccept = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccept.sizePolicy().hasHeightForWidth())
        self.btnAccept.setSizePolicy(sizePolicy)
        self.btnAccept.setDefault(True)
        self.btnAccept.setObjectName(_fromUtf8("btnAccept"))
        self.horizontalLayout.addWidget(self.btnAccept)
        self.tabWidget = QtGui.QTabWidget(DemolicionConstruccion)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 1001, 351))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 771, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cmbDemolicion = QtGui.QComboBox(self.groupBox_3)
        self.cmbDemolicion.setGeometry(QtCore.QRect(210, 38, 551, 25))
        self.cmbDemolicion.setObjectName(_fromUtf8("cmbDemolicion"))
        self.cmbDemolicion.addItem(_fromUtf8(""))
        self.cmbDemolicion.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 281, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(800, 20, 181, 91))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_56 = QtGui.QLabel(self.groupBox_7)
        self.label_56.setGeometry(QtCore.QRect(120, 40, 31, 19))
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.cmbPilotesAct = QtGui.QComboBox(self.groupBox_7)
        self.cmbPilotesAct.setGeometry(QtCore.QRect(20, 36, 91, 25))
        self.cmbPilotesAct.setObjectName(_fromUtf8("cmbPilotesAct"))
        self.cmbPilotesAct.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(50, 168, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(50, 22, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(50, 118, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(50, 219, 211, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(530, 123, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(529, 23, 181, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(530, 72, 221, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 263, 961, 51))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbCimentacion = QtGui.QLabel(self.tab_2)
        self.lbCimentacion.setGeometry(QtCore.QRect(280, 24, 221, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbCimentacion.setFont(font)
        self.lbCimentacion.setObjectName(_fromUtf8("lbCimentacion"))
        self.lbEstructura = QtGui.QLabel(self.tab_2)
        self.lbEstructura.setGeometry(QtCore.QRect(280, 71, 221, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbEstructura.setFont(font)
        self.lbEstructura.setObjectName(_fromUtf8("lbEstructura"))
        self.lbCubierta = QtGui.QLabel(self.tab_2)
        self.lbCubierta.setGeometry(QtCore.QRect(280, 119, 221, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbCubierta.setFont(font)
        self.lbCubierta.setObjectName(_fromUtf8("lbCubierta"))
        self.lbAlturaMedia = QtGui.QLabel(self.tab_2)
        self.lbAlturaMedia.setGeometry(QtCore.QRect(280, 168, 121, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbAlturaMedia.setFont(font)
        self.lbAlturaMedia.setObjectName(_fromUtf8("lbAlturaMedia"))
        self.lbAlturaTotal = QtGui.QLabel(self.tab_2)
        self.lbAlturaTotal.setGeometry(QtCore.QRect(280, 218, 191, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbAlturaTotal.setFont(font)
        self.lbAlturaTotal.setObjectName(_fromUtf8("lbAlturaTotal"))
        self.lbSuperficie = QtGui.QLabel(self.tab_2)
        self.lbSuperficie.setGeometry(QtCore.QRect(760, 23, 151, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbSuperficie.setFont(font)
        self.lbSuperficie.setObjectName(_fromUtf8("lbSuperficie"))
        self.lbPlantasBajoRasante = QtGui.QLabel(self.tab_2)
        self.lbPlantasBajoRasante.setGeometry(QtCore.QRect(761, 72, 141, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbPlantasBajoRasante.setFont(font)
        self.lbPlantasBajoRasante.setObjectName(_fromUtf8("lbPlantasBajoRasante"))
        self.lbPlantasSobreRasante = QtGui.QLabel(self.tab_2)
        self.lbPlantasSobreRasante.setGeometry(QtCore.QRect(760, 122, 151, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbPlantasSobreRasante.setFont(font)
        self.lbPlantasSobreRasante.setObjectName(_fromUtf8("lbPlantasSobreRasante"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(DemolicionConstruccion)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DemolicionConstruccion)

    def retranslateUi(self, DemolicionConstruccion):
        DemolicionConstruccion.setWindowTitle(_translate("DemolicionConstruccion", "Herevea", None))
        self.label_31.setText(_translate("DemolicionConstruccion", "Direccion", None))
        self.label_32.setText(_translate("DemolicionConstruccion", "Ref. Catastral", None))
        self.pushButton.setText(_translate("DemolicionConstruccion", "< Atrás", None))
        self.btnAccept.setText(_translate("DemolicionConstruccion", "Calculo de Huella Ecológica", None))
        self.groupBox_3.setTitle(_translate("DemolicionConstruccion", "Actuaciones", None))
        self.cmbDemolicion.setItemText(0, _translate("DemolicionConstruccion", "Edificio con estructura de muros fábrica m.mecánicos", None))
        self.cmbDemolicion.setItemText(1, _translate("DemolicionConstruccion", "Edificio con estructura de hormigón m.mecánicos", None))
        self.label_5.setText(_translate("DemolicionConstruccion", "Demolición Completa", None))
        self.groupBox_7.setTitle(_translate("DemolicionConstruccion", "Grado de actuación", None))
        self.label_56.setText(_translate("DemolicionConstruccion", "%", None))
        self.cmbPilotesAct.setItemText(0, _translate("DemolicionConstruccion", "100", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DemolicionConstruccion", "Demolición", None))
        self.label_7.setText(_translate("DemolicionConstruccion", "Altura media por planta:", None))
        self.label_4.setText(_translate("DemolicionConstruccion", "Cimentación:", None))
        self.label_6.setText(_translate("DemolicionConstruccion", "Estructura:", None))
        self.label_8.setText(_translate("DemolicionConstruccion", "Cubierta:", None))
        self.label_9.setText(_translate("DemolicionConstruccion", "Altura del edificio:", None))
        self.label_10.setText(_translate("DemolicionConstruccion", "Nº plantas sobre rasante:", None))
        self.label_2.setText(_translate("DemolicionConstruccion", "Superficie construida:", None))
        self.label.setText(_translate("DemolicionConstruccion", "Nº plantas bajo rasante:", None))
        self.label_3.setText(_translate("DemolicionConstruccion", "El nuevo edificio será ejecutado según las mismas características constructivas del proyecto original y con materiales de calidad media", None))
        self.lbCimentacion.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbEstructura.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbCubierta.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbAlturaMedia.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbAlturaTotal.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbSuperficie.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbPlantasBajoRasante.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.lbPlantasSobreRasante.setText(_translate("DemolicionConstruccion", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DemolicionConstruccion", "Nueva construcción", None))
