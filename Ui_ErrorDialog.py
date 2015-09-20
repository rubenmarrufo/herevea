"""
/***************************************************************************
Name			 	 : Herevea plugin
Description          : Herramienta del proyecto Herevea
Date                 : 22/May/15 
copyright            : (C) 2015 by Ruben Jimenez Marrufo
email                : ruben_marrufo@hotmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
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