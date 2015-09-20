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
from Ui_SeleccionForm import Ui_SeleccionForm
from Ui_ErrorDialog import Ui_ErrorDialog
from ParcelaService import ParcelaService

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Ui_SeleccionFormDialog(QtGui.QDialog):
  def __init__(self, catastroService): 
    QtGui.QDialog.__init__(self)
    # Set up the user interface from Designer.
    self.isValid=True  
    self.catastroService = catastroService   
    self.parcelaService = None
    self.ui = Ui_SeleccionForm()
    self.ui.setupUi(self)    
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.dialogOk)
    provincias = ['SEVILLA','HUELVA','CADIZ', 'CORDOBA', 'MALAGA','JAEN','GRANADA','ALMERIA']
    self.ui.cmbProvincia.addItems(provincias)
    self.onProvinciaSelected()
    self.connect(self.ui.cmbProvincia, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.onProvinciaSelected)

  def provincia(self):
    return self.ui.cmbProvincia.currentText()

  def municipio(self):
    return self.ui.cmbMunicipio.currentText()
    
  def dialogOk(self):
    isValid=True 
    if self.ui.radCatastro.isChecked():
        try:
            self.parcelaService = ParcelaService(self,self.ui.cmbProvincia.currentText(), self.ui.cmbMunicipio.currentText())
            self.parcelaService.initRefCatastral(self.ui.tbxRefCatastral.text())            
        except Exception as ex:
            print ex
            error = Ui_ErrorDialog('No se pudo encontrar una parcela con la referencia catastral ' + self.ui.tbxRefCatastral.text() + ' en la localidad seleccionado')
            error.show()
            error.exec_()
            isValid=False
    elif self.ui.radCoordenadas.isChecked():
        try:
            self.parcelaService = ParcelaService(self,self.ui.cmbProvincia.currentText(), self.ui.cmbMunicipio.currentText())
            self.parcelaService.initCoords(self.ui.tbxLong.text().replace(',','.'), self.ui.tbxLat.text().replace(',','.'))
        except Exception as ex:
            print ex
            error = Ui_ErrorDialog('No se pudo encontrar una parcela en las coordenadas introducidas en la localidad seleccionada')
            error.show()
            error.exec_()
            isValid=False            

  def closeEvent(self, evnt):
    if self.isValid:
        super(MyDialog, self).closeEvent(evnt)
    else:
        evnt.ignore()   
        isValid=True     
        
  def onProvinciaSelected(self):
    self.ui.cmbMunicipio.clear()
    if(self.ui.cmbProvincia.currentText() != ''):
        municipios = self.catastroService.getMunicipios(self.ui.cmbProvincia.currentText())
        for mun in municipios:    
            self.ui.cmbMunicipio.addItem(_fromUtf8(mun['nm']))