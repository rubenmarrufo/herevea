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
from Ui_UsuarioForm import Ui_UsuarioForm

class Ui_UsuarioFormDialog(QtGui.QDialog):
  def __init__(self, catastroService): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.back=False
    self.ui = Ui_UsuarioForm()
    self.ui.setupUi(self)    
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Siguiente >')
    
    self.ui.tbxDireccion.setText(catastroService.getDireccion())
    self.ui.tbxRefCatastral.setText(catastroService.getNumCatastro())
    self.ui.pushButton.clicked.connect(self.backButton)    
    
  def backButton(self):
    self.back=True
    self.close()
    
  def getValues(self):
    return {'Cimentacion': self.ui.cbCimentacion.currentText(), \
            'Estructura': self.ui.cbEstructura.currentText(), \
            'Cubierta': self.ui.cbCubierta.currentText(), \
            'Altura': self.ui.spbAlturaTotal.value(), \
            'AlturaPlanta': self.ui.spbAlturaMedia.value() }