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
from Ui_ResultForm import Ui_ResultForm
import locale

class Ui_ResultFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService, huellaResult): 
    QtGui.QDialog.__init__(self)
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ResultForm()
    self.ui.setupUi(self)
        
    self.ui.tabWidget.setCurrentIndex(0)
    self.ui.tbxDireccion.setText(parcelaService.getDireccion())
    self.ui.tbxRefCatastral.setText(parcelaService.getNumCatastro())
    
    self.ui.tabHERehParcial.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Energia"],4)))
    self.ui.tabHERehParcial.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Energia"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHERehParcial.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Bosques"],4)))
    self.ui.tabHERehParcial.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Bosques"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHERehParcial.setItem(0, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Pastos"],4)))
    self.ui.tabHERehParcial.setItem(1, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Pastos"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHERehParcial.setItem(0, 3, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Mar"],4)))
    self.ui.tabHERehParcial.setItem(1, 3, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Mar"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHERehParcial.setItem(0, 4, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Cultivos"],4)))
    self.ui.tabHERehParcial.setItem(1, 4, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Cultivos"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHERehParcial.setItem(0, 5, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["SuperficieConsumida"],4)))
    self.ui.tabHERehParcial.setItem(1, 5, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["SuperficieConsumida"] * parcelaService.getSuperficie(),2)))
    
    self.ui.tabHERehTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHERehTotal.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),2)))
    
    self.ui.tabHEComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHEComp.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),2)))
        
    self.ui.tabPEMReh.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    self.ui.tabPEMDem.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"],2)))
    self.ui.tabPEMCons.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Construccion"],2)))
    self.ui.tabPEMCons.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Construccion"] * parcelaService.getSuperficie(),2)))
        
    self.ui.tabPEMComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    self.ui.tabPEMComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"] + huellaResult["Construccion"] * parcelaService.getSuperficie(),2)))
    
  def toSpanishFormat(self, value, digits):
    digitStr=str(digits)
    return ('{:,.' + digitStr + 'f}').format(value).replace(',','_').replace('.',',').replace('_', '.')      