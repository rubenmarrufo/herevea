from PyQt4 import QtCore, QtGui 
from Ui_SeleccionForm import Ui_SeleccionForm
from Ui_ErrorDialog import Ui_ErrorDialog
from ParcelaService import ParcelaService
import csv
import os
from qgis.core import * 
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
    self.ui.btnAccept.clicked.connect(self.dialogOk)
    self.ui.btnCancel.clicked.connect(self.dialogOk)
    provincias = ['SEVILLA','HUELVA','CADIZ', 'CORDOBA', 'MALAGA','JAEN','GRANADA','ALMERIA']
    self.ui.cmbProvincia.addItems(provincias)
    self.onProvinciaSelected()
    self.connect(self.ui.cmbProvincia, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.onProvinciaSelected)

  def provincia(self):
    return self.ui.cmbProvincia.currentText()

  def municipio(self):
    return self.ui.cmbMunicipio.currentText()

  def coordenadas(self):
      if self.parcelaService == None: 
          try: 
              dir = os.path.dirname(__file__)
              filename = os.path.join(dir,'coordenadas.csv')    
              with open(filename, 'rb') as csvfile:
                  data = [row for row in csv.reader(csvfile.read().splitlines(), delimiter=';')]          
                  row = next(x for x in data if x[0].lower() == self.municipio().lower())              
                  return QgsPoint(float(row[2].replace(',','.')),float(row[1].replace(',','.')))
          except Exception as ex:  
                return None
      elif self.parcelaService.x != None and self.parcelaService.y != None:
          return QgsPoint(float(self.parcelaService.x),float(self.parcelaService.y))
        
  def zoom(self):
      if self.parcelaService == None:
          return 3000
      else:
          return 500
      
  def dialogOk(self):        
    if self.ui.radCatastro.isChecked():
        self.parcelaService = ParcelaService(self,self.ui.cmbProvincia.currentText(), self.ui.cmbMunicipio.currentText())
        self.parcelaService.initRefCatastral(self.ui.tbxRefCatastral.text())                 
    elif self.ui.radCoordenadas.isChecked():
        self.parcelaService = ParcelaService(self,self.ui.cmbProvincia.currentText(), self.ui.cmbMunicipio.currentText())
        self.parcelaService.initCoords(self.ui.tbxLong.text().replace(',','.'), self.ui.tbxLat.text().replace(',','.'))
    else:
        self.parcelaService = None        
    self.accept()
        
  def onProvinciaSelected(self):
    self.ui.cmbMunicipio.clear()
    if(self.ui.cmbProvincia.currentText() != ''):
        municipios = self.catastroService.getMunicipios(self.ui.cmbProvincia.currentText())
        for mun in municipios:    
            self.ui.cmbMunicipio.addItem(_fromUtf8(mun['nm']))