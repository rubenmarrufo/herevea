import time
from PyQt4 import QtCore, QtGui
from ParcelaService import ParcelaService

class Ui_ProgressDialog(QtGui.QDialog):
    
    def __init__(self, x, y, parent=None):
        super(Ui_ProgressDialog, self).__init__(parent)
        
        self.thread = ParcelaService(x,y)
        
        self.nameLabel = QtGui.QLabel("Obteniendo informacion del catastro...   ")
        self.nameLine = QtGui.QLineEdit()
        
        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(0)
        
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.progressbar, 1, 0)
        mainLayout.addWidget(self.nameLabel, 0, 0)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Procesando")
                
        self.thread.procDone.connect(self.fin)        
        self.thread.start()
        
    def fin(self):
        self.close()    
    
    def getParcelaService(self):
        return self.thread    
 ##self.hide()           
