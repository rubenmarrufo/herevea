from PyQt4 import QtCore, QtGui 
from Ui_Error import Ui_Error
import os

class Ui_ErrorDialog(QtGui.QDialog):
  def __init__(self, error): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_Error()
    self.ui.setupUi(self)
    dir = os.path.dirname(__file__)
    icon_path = os.path.join(dir,'img\Warning.png')  
    self.ui.image.setPixmap(QtGui.QPixmap(icon_path))
    
    self.ui.label.setText(error)    