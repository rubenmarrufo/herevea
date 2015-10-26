# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_IntroForm.ui'
#
# Created: Mon Oct 19 22:08:43 2015
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

class Ui_IntroForm(object):
    def setupUi(self, IntroForm):
        IntroForm.setObjectName(_fromUtf8("IntroForm"))
        IntroForm.resize(957, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Herevea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IntroForm.setWindowIcon(icon)
        self.label_31 = QtGui.QLabel(IntroForm)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbxDireccion = QtGui.QLineEdit(IntroForm)
        self.tbxDireccion.setGeometry(QtCore.QRect(96, 20, 501, 25))
        self.tbxDireccion.setReadOnly(True)
        self.tbxDireccion.setObjectName(_fromUtf8("tbxDireccion"))
        self.tbxRefCatastral = QtGui.QLineEdit(IntroForm)
        self.tbxRefCatastral.setGeometry(QtCore.QRect(730, 20, 211, 25))
        self.tbxRefCatastral.setReadOnly(True)
        self.tbxRefCatastral.setObjectName(_fromUtf8("tbxRefCatastral"))
        self.label_32 = QtGui.QLabel(IntroForm)
        self.label_32.setGeometry(QtCore.QRect(623, 20, 101, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.groupBox = QtGui.QGroupBox(IntroForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 921, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 821, 242))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnRehab = QtGui.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRehab.sizePolicy().hasHeightForWidth())
        self.btnRehab.setSizePolicy(sizePolicy)
        self.btnRehab.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.btnRehab.setFont(font)
        self.btnRehab.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnRehab.setObjectName(_fromUtf8("btnRehab"))
        self.horizontalLayout_2.addWidget(self.btnRehab)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.btnDemCons = QtGui.QToolButton(self.verticalLayoutWidget)
        self.btnDemCons.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.btnDemCons.setFont(font)
        self.btnDemCons.setObjectName(_fromUtf8("btnDemCons"))
        self.horizontalLayout_2.addWidget(self.btnDemCons)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtGui.QPushButton(IntroForm)
        self.pushButton.setGeometry(QtCore.QRect(820, 360, 112, 34))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(IntroForm)
        QtCore.QMetaObject.connectSlotsByName(IntroForm)

    def retranslateUi(self, IntroForm):
        IntroForm.setWindowTitle(_translate("IntroForm", "Herevea", None))
        self.label_31.setText(_translate("IntroForm", "Direccion", None))
        self.label_32.setText(_translate("IntroForm", "Ref. Catastral", None))
        self.label.setText(_translate("IntroForm", "Comparativa económica y ambiental de la rehabilitación o demolición y nueva construcción de edificios residenciales", None))
        self.btnRehab.setText(_translate("IntroForm", "Rehabilitación", None))
        self.label_2.setText(_translate("IntroForm", "  VS  ", None))
        self.btnDemCons.setText(_translate("IntroForm", "Demolición \n"
"+\n"
"Nueva Construcción", None))
        self.pushButton.setText(_translate("IntroForm", "< Atrás", None))

