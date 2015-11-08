# encoding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from Ui_ResultForm import Ui_ResultForm
import locale
import pyqtgraph as pg
import numpy as np
import math
import subprocess
import json
import os
import PyQt4
from collections import OrderedDict
from ConfigService import ConfigService

class Ui_ResultFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService, huellaResult): 
    QtGui.QDialog.__init__(self)
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    
    pg.setConfigOption('background', QtGui.QColor(0, 0, 0, 0))
    pg.setConfigOption('foreground', 'k')
    
    self.back=False
    self.huellaResult = huellaResult
    # Set up the user interface from Designer. 
    self.ui = Ui_ResultForm()
    self.ui.setupUi(self)
    self.ui.tabWidget.setCurrentIndex(0)
    self.ui.tbxDireccion.setText(parcelaService.getDireccion())
    self.ui.tbxRefCatastral.setText(parcelaService.getNumCatastro())    
    self.ui.btnReport.clicked.connect(self.openReport)

    self.setStyles()    
    self.addEnergiaPieChart(huellaResult, parcelaService)
    self.addHEParcial(huellaResult, parcelaService)
        
    self.ui.tabHERehTotal.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabHERehTotal.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),3)))
    self.ui.tabHERehTotal.item(0, 0).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabHERehTotal.item(0, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    
    self.ui.tabDemConsComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["DemolicionHESuperficie"],4)))
    self.ui.tabDemConsComp.setItem(1, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["ConstruccionHESuperficie"],4)))
    self.ui.tabDemConsComp.setItem(2, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["DemolicionHESuperficie"] + huellaResult["ConstruccionHESuperficie"],4)))
    self.ui.tabDemConsComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["DemolicionHE"],3)))
    self.ui.tabDemConsComp.setItem(1, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["ConstruccionHE"],3)))
    self.ui.tabDemConsComp.setItem(2, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["DemolicionHE"] + huellaResult["ConstruccionHE"],3)))
    self.ui.tabDemConsComp.setItem(0, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"],2)))
    self.ui.tabDemConsComp.setItem(1, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Construccion"],2)))
    self.ui.tabDemConsComp.setItem(2, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Demolicion"] + huellaResult["Construccion"],2)))
    self.ui.tabDemConsComp.item(0, 0).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(1, 0).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(2, 0).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(0, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(1, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(2, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(0, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(1, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabDemConsComp.item(2, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    
    self.ui.tabRehComp.setItem(0, 0, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"],4)))
    self.ui.tabRehComp.setItem(0, 1, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Total"] * parcelaService.getSuperficie(),3)))
    self.ui.tabRehComp.setItem(0, 2, QtGui.QTableWidgetItem(self.toSpanishFormat(huellaResult["Rehabilitacion"],2)))
    self.ui.tabRehComp.item(0, 0).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabRehComp.item(0, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    self.ui.tabRehComp.item(0, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
    self.ui.pushButton.clicked.connect(self.backButton)    
    
  def backButton(self):
    self.back=True
    self.close()
    
  def openReport(self):
    config = ConfigService()
    dir = unicode(config.getPath()) 
    application = os.path.join(dir,u'Informes\\',unicode(self.huellaResult["ReportPath"]))    
    cmd = [unicode(application)]
    process = subprocess.Popen(cmd, shell=True)
    
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
    
    pie = PieChartItem(OrderedDict([('Maquinaria',maquinaria/total), ('Electricidad',electricidad/total), ('Agua',agua/total), ('Alimentos',alimentos/total), ('Movilidad',movilidad/total), ('Residuos RSU',residuosRSU/total), ('Materiales',materiales/total), ('Residuos RCD',residuosRCD/total )]))
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
        
    self.ui.tabDemConsComp.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabDemConsComp.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabDemConsComp.horizontalHeader().setVisible(True)
    self.ui.tabDemConsComp.verticalHeader().setVisible(True)
    
    self.ui.tabRehComp.horizontalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabRehComp.verticalHeader().setStyleSheet("background-color: rgb(51, 153, 51);\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);");
    self.ui.tabRehComp.horizontalHeader().setVisible(False)
    self.ui.tabRehComp.verticalHeader().setVisible(True)
    
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
        colours = {'Maquinaria':QtGui.QColor(102, 153, 0, 255), \
                   'Electricidad':QtGui.QColor(236, 118, 124, 255), \
                   'Agua':QtGui.QColor(255, 192, 0, 255), \
                   'Alimentos':QtGui.QColor(71, 75, 120, 255), \
                   'Movilidad':QtGui.QColor(23, 193, 0, 255),\
                   'Residuos RSU':QtGui.QColor(45, 162, 191, 255),\
                   'Materiales':QtGui.QColor(57, 199, 157, 255),\
                   'Residuos RCD':QtGui.QColor(235, 100, 27, 255)}    
        for d in self.data.keys():  
            angle = self.data[d] * 360 * 16
            ellipse = QtGui.QGraphicsEllipseItem(0, 0, 200, 200)
            ellipse.setPos(200, 0)
            ellipse.setStartAngle(set_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(colours[d])
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