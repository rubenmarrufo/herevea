# encoding=utf-8
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
import pyqtgraph as pg
import numpy as np
import math
import subprocess
import json
import os

class Ui_ResultFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService, huellaResult): 
    QtGui.QDialog.__init__(self)
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    
    pg.setConfigOption('background', QtGui.QColor(0, 0, 0, 0))
    pg.setConfigOption('foreground', 'k')
    
    self.huellaResult = huellaResult
    # Set up the user interface from Designer. 
    self.ui = Ui_ResultForm()
    self.ui.setupUi(self)
    self.ui.tabWidget.setCurrentIndex(0)
    self.ui.tbxDireccion.setText(parcelaService.getDireccion())
    self.ui.tbxRefCatastral.setText(parcelaService.getNumCatastro())
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Generar Informe')
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openReport)

    self.setStyles()    
    self.addEnergiaPieChart(huellaResult, parcelaService)
    self.addHEParcial(huellaResult, parcelaService)
        
    self.ui.tabHERehTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHERehTotal.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),3)))
    
    self.ui.tabHEDemConsTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEDemolicion"],4)))
    self.ui.tabHEDemConsTotal.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEDemolicion"] * parcelaService.getSuperficie(),3)))
    self.ui.tabHEDemConsTotal.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"],4)))
    self.ui.tabHEDemConsTotal.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"] * parcelaService.getSuperficie(),3)))
    
    self.ui.tabHEComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHEComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),3)))
    self.ui.tabHEComp.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["HEConstruccion"] + huellaResult["HEDemolicion"],4)))
    self.ui.tabHEComp.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat((huellaResult["HEConstruccion"] + huellaResult["HEDemolicion"]) * parcelaService.getSuperficie(),3)))
        
    self.ui.tabPEMReh.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    
    self.ui.tabPEMDemCons.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"],2)))
    self.ui.tabPEMDemCons.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Construccion"],2)))
            
    self.ui.tabPEMComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    self.ui.tabPEMComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"] + huellaResult["Construccion"],2)))

  def openReport(self):    
    dir = os.path.dirname(__file__)
    application = os.path.join(dir,'Informes/',self.huellaResult["ReportPath"])
    cmd = [application]
    print cmd
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    
  def addEnergiaPieChart(self, huellaResult, parcelaService):    
    #maquinaria = 1
    #electricidad = 5
    #agua = 3
    #alimentos = 2
    #movilidad = 6
    #residuosRSU = 2
    #materiales = 2
    #residuosRCD = 5
    
    maquinaria = huellaResult["Maquinaria"] * parcelaService.getSuperficie()
    electricidad = huellaResult["Electricidad"] * parcelaService.getSuperficie()
    agua = huellaResult["Agua"] * parcelaService.getSuperficie()
    alimentos = huellaResult["Alimentos"] * parcelaService.getSuperficie()
    movilidad = huellaResult["Movilidad"] * parcelaService.getSuperficie()
    residuosRSU = huellaResult["Residuos RSU"] * parcelaService.getSuperficie()
    materiales = huellaResult["Materiales"] * parcelaService.getSuperficie()
    residuosRCD = huellaResult["Residuos RCD"] * parcelaService.getSuperficie()
    
    total=float(maquinaria+electricidad+agua+alimentos+movilidad+residuosRSU+materiales+residuosRCD)
    
    pie = PieChartItem({'Maquinaria':maquinaria/total, 'Electricidad':electricidad/total, 'Agua':agua/total, 'Alimentos':alimentos/total, 'Movilidad':movilidad/total, 'Residuos RSU':residuosRSU/total, 'Materiales':materiales/total, 'Residuos RCD':residuosRCD/total })
    self.ui.pieChart.addItem(pie)
  
  def addHEParcial(self, huellaResult, parcelaService):
    #energia = 1
    #bosques = 5
    #pastos = 3
    #mar = 2
    #cultivos = 6
    #superficieConsumida = 2

    energia = huellaResult["Energia"] * parcelaService.getSuperficie()    
    bosques = huellaResult["Bosques"] * parcelaService.getSuperficie()    
    pastos = huellaResult["Pastos"] * parcelaService.getSuperficie()    
    mar = huellaResult["Mar"] * parcelaService.getSuperficie()    
    cultivos = huellaResult["Cultivos"] * parcelaService.getSuperficie()    
    superficieConsumida = huellaResult["SuperficieConsumida"] * parcelaService.getSuperficie()
    
    self.ui.chartHEParcial.getAxis('bottom').setTicks([[(0, 'Energia'), (20, 'Bosques'), (40, 'Pastos'), (60, 'Mar'), (80, 'Cultivos'), (100, 'Sup.Cons.')]])
    
    x = np.arange(1)
    bgEnergia = pg.BarGraphItem(x=x, height=energia, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    bgBosques = pg.BarGraphItem(x=x + 20, height=bosques, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    bgPastos = pg.BarGraphItem(x=x + 40, height=pastos, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    bgMar = pg.BarGraphItem(x=x + 60, height=mar, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    bgCultivos = pg.BarGraphItem(x=x + 80, height=cultivos, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    bgSuperficie = pg.BarGraphItem(x=x + 100, height=superficieConsumida, width=10, brush=QtGui.QColor(0, 176, 80, 255))
    
    self.ui.chartHEParcial.addItem(bgEnergia)
    self.ui.chartHEParcial.addItem(bgBosques)
    self.ui.chartHEParcial.addItem(bgPastos)
    self.ui.chartHEParcial.addItem(bgMar)
    self.ui.chartHEParcial.addItem(bgCultivos)
    self.ui.chartHEParcial.addItem(bgSuperficie)

  
  def toSpanishFormat(self, value, digits):
    if(value==0):
        return '-'   
    digitStr = str(digits)    
    return ('{:,.' + digitStr + 'f}').format(value).replace(',', '_').replace('.', ',').replace('_', '.')

  def setStyles(self):
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
    
class PieChartItemRegion:
    def __init__(self, ellipse, x, y, text): 
        self.ellipse = ellipse
        self.text = text
        self.x = x
        self.y = y
        


class PieChartItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  
        self.txt = QtGui.QGraphicsSimpleTextItem("Test")
        self.ellipseList = list()
        self.textList = list()
        set_angle = 0
        count1 = 0 
        colours = [QtGui.QColor(102, 153, 0, 255), \
                   QtGui.QColor(236, 118, 124, 255), \
                   QtGui.QColor(255, 192, 0, 255), \
                   QtGui.QColor(71, 75, 120, 255), \
                   QtGui.QColor(23, 193, 0, 255),\
                   QtGui.QColor(45, 162, 191, 255),\
                   QtGui.QColor(57, 199, 157, 255),\
                   QtGui.QColor(235, 100, 27, 255)]    
        for d in self.data.keys():     
            angle = self.data[d] * 360 * 16
            ellipse = QtGui.QGraphicsEllipseItem(0, 0, 200, 200)
            ellipse.setPos(200, 0)
            ellipse.setStartAngle(set_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(colours[count1])
            set_angle = set_angle + angle
            
            count1 += 1
            x = 90 + 70 * math.cos((set_angle - angle / 2) / 16 * 0.0174)
            y = 90 - 70 * math.sin((set_angle - angle / 2) / 16 * 0.0174)
            
            self.ellipseList.append(PieChartItemRegion(ellipse, x, y, self.data[d]))               
    
    def paint(self, p, *args):
        for el in self.ellipseList:
           el.ellipse.paint(p, *args)
        for el in self.ellipseList:
           font = p.font();
           font.setPointSize(6);
           p.setFont(font);
           if el.text > 0.03:
               textLabel = self.toSpanishFormat(el.text*100,1)+'%'
               p.drawText(QtCore.QRectF(el.x, el.y, 100, 100), textLabel)           
        
    def boundingRect(self):
        """Returns the bounding rectangle of the data.
        
        For the y boundaries, uses low/high if they are used, or open/close
        otherwise.
        """
        return QtCore.QRectF(0, 0, 600, 600)
    
    def toSpanishFormat(self, value, digits):    
        digitStr = str(digits)    
        return ('{:,.' + digitStr + 'f}').format(value).replace(',', '_').replace('.', ',').replace('_', '.')   