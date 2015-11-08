from PyQt4 import QtCore, QtGui 
from Ui_ConfiguracionForm import Ui_ConfiguracionForm
from Ui_ErrorDialog import Ui_ErrorDialog

class Ui_ConfiguracionFormDialog(QtGui.QDialog):
  def __init__(self, configService): 
    QtGui.QDialog.__init__(self) 
    
    # Set up the user interface from Designer.
    self.back=False 
    self.ui = Ui_ConfiguracionForm()
    self.ui.setupUi(self)
    self.configService = configService
    self.ui.tbxPath.setText(self.configService.getPath())
    self.ui.btnAccept.clicked.connect(self.save)
    self.ui.btnCancel.clicked.connect(self.cancel)
    
  def save(self):
    if self.configService.validatePath(self.ui.tbxPath.text()):
        self.configService.savePath(self.ui.tbxPath.text())
        self.accept()
    else:
        ui_Error=Ui_ErrorDialog(u'No se pudo acceder a la carpeta seleccionada')
        ui_Error.show()
        ui_Error.exec_()
        
  def cancel(self):
      self.close()    