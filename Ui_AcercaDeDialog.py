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
from Ui_AcercaDe import Ui_AcercaDe
import os

class Ui_AcercaDeDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    
    self.ui = Ui_AcercaDe()
    self.ui.setupUi(self)
    dir = os.path.dirname(__file__)
    icon_path = os.path.join(dir,'img\all.png')  
    self.ui.label_2.setPixmap(QtGui.QPixmap(icon_path))    