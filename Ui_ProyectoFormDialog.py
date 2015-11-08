from PyQt4 import QtCore, QtGui 
from Ui_ProyectoForm import Ui_ProyectoForm

class Ui_ProyectoFormDialog(QtGui.QDialog):
  def __init__(self, parcelaService): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ProyectoForm()
    self.ui.setupUi(self)
    self.parcelaService = parcelaService
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
    
  def getValues(self):
    return {'Provincia':self.parcelaService.provincia, \
            'Municipio':self.parcelaService.municipio, \
            'Direccion':self.ui.tbxDireccion.text(), \
            'RefCatastral':self.ui.tbxRefCatastral.text(), \
            'Superficie':self.ui.tbxSuperficie.value(), \
            'PlantasBajo': self.ui.tbxPlantasBajoRasante.text(), \
            'PlantasSobre': self.ui.tbxPlantasSobreRasante.text(), \
            'PlantaBajaViviendas': 'si' if self.ui.radViviendas.isChecked() else 'no' }
