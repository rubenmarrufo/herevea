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
from pyqtgraph import *
import numpy as np

class Ui_ResultFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService, huellaResult): 
    QtGui.QDialog.__init__(self)
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ResultForm()
    self.ui.setupUi(self)
    self.ui.tabWidget.setCurrentIndex(0)
    #self.ui.tbxDireccion.setText(parcelaService.getDireccion())
    #self.ui.tbxRefCatastral.setText(parcelaService.getNumCatastro())
    self.ui.tabHERehTotal.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHERehTotal.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHERehTotal.horizontalHeader().setVisible(True)
    self.ui.tabHERehTotal.verticalHeader().setVisible(True)
        
    self.ui.tabHEDemConsTotal.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHEDemConsTotal.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHEDemConsTotal.horizontalHeader().setVisible(True)
    self.ui.tabHEDemConsTotal.verticalHeader().setVisible(True)    
    
    self.ui.tabHEComp.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHEComp.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabHEComp.horizontalHeader().setVisible(True)
    self.ui.tabHEComp.verticalHeader().setVisible(True)
        
    self.ui.tabPEMReh.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");  
    self.ui.tabPEMReh.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");  
    self.ui.tabPEMReh.horizontalHeader().setVisible(True)
    self.ui.tabPEMReh.verticalHeader().setVisible(True)
    
    self.ui.tabPEMDemCons.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabPEMDemCons.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabPEMDemCons.horizontalHeader().setVisible(True)
    self.ui.tabPEMDemCons.verticalHeader().setVisible(True)    
    
    self.ui.tabPEMComp.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabPEMComp.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabPEMComp.horizontalHeader().setVisible(True)
    self.ui.tabPEMComp.verticalHeader().setVisible(True)
    
    
    
    #stylesheet = "::section{gridline-color:rgb(255, 255, 255);border-color: rgb(255, 255, 255);}"
    #self.ui.tabHERehTotal.horizontalHeader().setStyleSheet(stylesheet)

    #self.ui.win = PlotWidget(self.ui.frame)
    #self.ui.win.setGeometry(QtCore.QRect(239, 219, 651, 301))
    #self.ui.win.setWindowTitle('pyqtgraph example: BarGraphItem')
    
    #x = np.arange(10)
    #y1 = np.sin(x)
    #y2 = 1.1 * np.sin(x+1)
    #y3 = 1.2 * np.sin(x+2)
    
    #bg1 = BarGraphItem(x=x, height=y1, width=0.3, brush='r')
    #bg2 = BarGraphItem(x=x+0.33, height=y2, width=0.3, brush='g')
    #bg3 = BarGraphItem(x=x+0.66, height=y3, width=0.3, brush='b')
    
    #self.ui.win.addItem(bg1)
    #self.ui.win.addItem(bg2)
    #self.ui.win.addItem(bg3)
    
    
    #self.ui.tabHERehParcial.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Energia"],4)))
    #self.ui.tabHERehParcial.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Energia"] * parcelaService.getSuperficie(),2)))
    #self.ui.tabHERehParcial.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Bosques"],4)))
    #self.ui.tabHERehParcial.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Bosques"] * parcelaService.getSuperficie(),2)))
    #self.ui.tabHERehParcial.setItem(0, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Pastos"],4)))
    #self.ui.tabHERehParcial.setItem(1, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Pastos"] * parcelaService.getSuperficie(),2)))
    #self.ui.tabHERehParcial.setItem(0, 3, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Mar"],4)))
    #self.ui.tabHERehParcial.setItem(1, 3, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Mar"] * parcelaService.getSuperficie(),2)))
    #self.ui.tabHERehParcial.setItem(0, 4, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Cultivos"],4)))
    #self.ui.tabHERehParcial.setItem(1, 4, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Cultivos"] * parcelaService.getSuperficie(),2)))
    #self.ui.tabHERehParcial.setItem(0, 5, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["SuperficieConsumida"],4)))
    #self.ui.tabHERehParcial.setItem(1, 5, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["SuperficieConsumida"] * parcelaService.getSuperficie(),2)))
    
    self.ui.tabHERehTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHERehTotal.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),2)))
    
    self.ui.tabHEDemConsTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEDemolicion"],4)))
    self.ui.tabHEDemConsTotal.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEDemolicion"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHEDemConsTotal.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"],4)))
    self.ui.tabHEDemConsTotal.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"] * parcelaService.getSuperficie(),2)))
    
    self.ui.tabHEComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHEComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),2)))
    self.ui.tabHEComp.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"] + huellaResult["HEDemolicion"],4)))
    self.ui.tabHEComp.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat((huellaResult["HEConstruccion"] + huellaResult["HEDemolicion"]) * parcelaService.getSuperficie(),2)))
        
    self.ui.tabPEMReh.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    
    self.ui.tabPEMDemCons.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"],2)))
    self.ui.tabPEMDemCons.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Construccion"],2)))
            
    self.ui.tabPEMComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    self.ui.tabPEMComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"] + huellaResult["Construccion"],2)))
    
  def toSpanishFormat(self, value, digits):    
    digitStr=str(digits)    
    return ('{:,.' + digitStr + 'f}').format(value).replace(',','_').replace('.',',').replace('_', '.')      