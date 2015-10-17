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
        self.demCons=False
        self.ui = Ui_IntroForm()
        self.ui.setupUi(self)
        self.ui.tbxDireccion.setText(catastroService.getDireccion())
        self.ui.tbxRefCatastral.setText(catastroService.getNumCatastro())
        self.ui.btnRehab.clicked.connect(self.rehabButton)    
        self.ui.btnDemCons.clicked.connect(self.demConsButton)
    
    def rehabButton(self):    
        self.rehab=True
        self.demCons=False
        self.accept()
    
    def demConsButton(self):    
        self.rehab=False
        self.demCons=True
        self.accept()
        
    def toRehab(self):
        self.ui.btnDemCons.setEnabled(False)
        self.ui.btnRehab.setEnabled(True)
    
    def toDemCons(self):
        self.ui.btnDemCons.setEnabled(True)
        self.ui.btnRehab.setEnabled(True)