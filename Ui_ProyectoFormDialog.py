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
from Ui_ProyectoForm import Ui_ProyectoForm

class Ui_ProyectoFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ProyectoForm()
    self.ui.setupUi(self)
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Siguiente >')
    
    self.ui.tbxDireccion.setText(parcelaService.getDireccion())
    self.ui.tbxRefCatastral.setText(parcelaService.getNumCatastro())
    self.ui.tbxAntiguedad.setMaximum(99999)
    self.ui.tbxAntiguedad.setValue(parcelaService.getAntiguedad())
    self.ui.cbTipoInmueble.setCurrentIndex(0 if parcelaService.isInmuebleUnico() else 1)
    self.ui.tbxUso.setText(parcelaService.uso())
    self.ui.tbxSuperficie.setMaximum(99999999)
    self.ui.tbxSuperficie.setValue(parcelaService.getSuperficie())
    self.ui.tbxPlantasBajoRasante.setValue(parcelaService.plantas()['plantasBajo'])
    self.ui.tbxPlantasSobreRasante.setValue(parcelaService.plantas()['plantasSobre'])        
    self.ui.radViviendas.setChecked(parcelaService.plantaBajoViviendas())
    self.ui.radOtrosUsos.setChecked(not parcelaService.plantaBajoViviendas())
    self.ui.tbxNInmuebles.setValue(parcelaService.numeroInmuebles())
