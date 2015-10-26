import time
from PyQt4 import QtCore, QtGui
from ParcelaService import ParcelaService
from PyQt4.QtGui import QProgressBar
from PyQt4.QtCore import *
from Ui_IntroForm import Ui_IntroForm

class Ui_IntroFormDialog(QtGui.QDialog):
    
    def __init__(self, catastroService):
        QtGui.QDialog.__init__(self) 
        
        self.rehab=False
        self.back=False
        self.demCons=False
        self.ui = Ui_IntroForm()
        self.ui.setupUi(self)
        self.ui.tbxDireccion.setText(catastroService.getDireccion())
        self.ui.tbxRefCatastral.setText(catastroService.getNumCatastro())
        self.ui.btnRehab.clicked.connect(self.rehabButton)    
        self.ui.btnDemCons.clicked.connect(self.demConsButton)
        self.ui.pushButton.clicked.connect(self.backButton)    
    
    def backButton(self):
        self.back=True
        self.close()
    
    def rehabButton(self):    
        self.toRehab()
        self.accept()
    
    def demConsButton(self):    
        self.toDemCons()
        self.accept()
        
    def toRehab(self):
        self.rehab=True
        self.demCons=False
        self.ui.btnDemCons.setEnabled(False)
        self.ui.btnRehab.setEnabled(True)
    
    def toDemCons(self):
        self.rehab=False
        self.demCons=True
        self.ui.btnDemCons.setEnabled(True)
        self.ui.btnRehab.setEnabled(True)