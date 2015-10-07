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
from Ui_ActuacionForm import Ui_ActuacionForm
from Ui_ErrorDialog import Ui_ErrorDialog

class Ui_ActuacionFormDialog(QtGui.QDialog):
  def __init__(self, catastroService): 
    QtGui.QDialog.__init__(self) 
    
    # Set up the user interface from Designer.
    self.back=False 
    self.ui = Ui_ActuacionForm()
    self.ui.setupUi(self)
    self.ui.btnAccept.clicked.connect(self.calcular)
    self.ui.tbxDireccion.setText(catastroService.getDireccion())
    self.ui.tbxRefCatastral.setText(catastroService.getNumCatastro())
    self.ui.tabWidget.setCurrentIndex(0)
    self.ui.pushButton.clicked.connect(self.backButton) 
    self.ui.cmbCubHorCom.currentIndexChanged.connect(self.cmbCubHorComChanged)
    self.ui.cmbCubIncCompleta.currentIndexChanged.connect(self.cmbCubIncComChanged)
    self.ui.cmbCarpLigera.currentIndexChanged.connect(self.cmbCarpLigeraChanged)
    self.ui.cmbCarpMadera.currentIndexChanged.connect(self.cmbCarpMaderaChanged)

  def calcular(self):
    if self.existActuaciones():
        self.accept()
    else:
        ui_Error=Ui_ErrorDialog('No se puede evaluar la Huella Ecologica ya que no se ha seleccionado ninguna actuacion')
        ui_Error.show()
        ui_Error.exec_()
    
  def backButton(self):
    self.back=True
    self.close()
    
  def cmbCubHorComChanged(self, index):
      if(index != 0):
          self.ui.cmbCubHorFaldon.setCurrentIndex(0)          
          self.ui.cmbCubHorEncParamVer.setCurrentIndex(0)          
          self.ui.cmbCubHorEncCazoletas.setCurrentIndex(0)
          self.ui.cmbCubHorFaldonAct.setCurrentIndex(0)          
          self.ui.cmbCubHorEncParamVerAct.setCurrentIndex(0)          
          self.ui.cmbCubHorEncCazoletasAct.setCurrentIndex(0)                  
      self.ui.cmbCubHorFaldon.setEnabled(False if index != 0 else True)
      self.ui.cmbCubHorEncParamVer.setEnabled(False if index != 0 else True)
      self.ui.cmbCubHorEncCazoletas.setEnabled(False if index != 0 else True)
      self.ui.cmbCubHorFaldonAct.setEnabled(False if index != 0 else True)
      self.ui.cmbCubHorEncParamVerAct.setEnabled(False if index != 0 else True)
      self.ui.cmbCubHorEncCazoletasAct.setEnabled(False if index != 0 else True)

  def cmbCubIncComChanged(self, index):
      if(index != 0):
          self.ui.cmbCubIncFaldon.setCurrentIndex(0)          
          self.ui.cmbCubIncEncParamVer.setCurrentIndex(0)          
          self.ui.cmbCubIncRemates.setCurrentIndex(0)
          self.ui.cmbCubIncFaldonAct.setCurrentIndex(0)          
          self.ui.cmbCubIncEncParamVerAct.setCurrentIndex(0)          
          self.ui.cmbCubIncRematesAct.setCurrentIndex(0)                  
      self.ui.cmbCubIncFaldon.setEnabled(False if index != 0 else True)
      self.ui.cmbCubIncEncParamVer.setEnabled(False if index != 0 else True)
      self.ui.cmbCubIncRemates.setEnabled(False if index != 0 else True)
      self.ui.cmbCubIncFaldonAct.setEnabled(False if index != 0 else True)
      self.ui.cmbCubIncEncParamVerAct.setEnabled(False if index != 0 else True)
      self.ui.cmbCubIncRematesAct.setEnabled(False if index != 0 else True)
      
  def cmbCarpLigeraChanged(self, index):
      if index != 0:
          self.ui.cmbCarpMadera.setCurrentIndex(0)          
          self.ui.cmbCarpMaderaAct.setCurrentIndex(0)                  
      self.ui.cmbCarpMadera.setEnabled(False if index != 0 else True)
      self.ui.cmbCarpMaderaAct.setEnabled(False if index != 0 else True)

  def cmbCarpMaderaChanged(self, index):
      if index != 0:
          self.ui.cmbCarpLigera.setCurrentIndex(0)          
          self.ui.cmbCarpLigeraAct.setCurrentIndex(0)                  
      self.ui.cmbCarpLigera.setEnabled(False if index != 0 else True)
      self.ui.cmbCarpLigeraAct.setEnabled(False if index != 0 else True)
                
  def setDatosUsuario(self, datosUsuario):
    if datosUsuario['Cubierta']=='Horizontal':
        self.ui.groupCubInc.setEnabled(False)
        self.ui.groupCubHor.setEnabled(True)
        self.ui.cmbCubIncCompleta.setCurrentIndex(0)
        self.ui.cmbCubIncFaldon.setCurrentIndex(0)          
        self.ui.cmbCubIncEncParamVer.setCurrentIndex(0)          
        self.ui.cmbCubIncRemates.setCurrentIndex(0)
    else:
        self.ui.groupCubInc.setEnabled(True)
        self.ui.groupCubHor.setEnabled(False)
        self.ui.cmbCubHorCom.setCurrentIndex(0)
        self.ui.cmbCubHorFaldon.setCurrentIndex(0)          
        self.ui.cmbCubHorEncParamVer.setCurrentIndex(0)          
        self.ui.cmbCubHorEncCazoletas.setCurrentIndex(0)
        
  def setDatosCatastro(self, datosCatastro):
    self.plantas = datosCatastro['PlantasSobre']
    
  def existActuaciones(self):
    return self.ui.cmbPilotes.currentText() != 'No hay actuaciones' or \
      self.ui.cmbArquetas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbColectores.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbBajantes.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbForjados.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbFisuras.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbGrietas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbLadFisuras.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbLadGrietas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbLadHumSuelo.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbLadHumTecho.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbIntFisuras.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbIntGrietas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbHumSuelo.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubHorCom.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubHorFaldon.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubHorEncParamVer.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubHorEncCazoletas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubIncCompleta.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubIncFaldon.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubIncRemates.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCubIncEncParamVer.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbClimatizacion.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbRadiadores.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCircuitos.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbLineasYDerivaciones.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbPuntosLuz.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbTomaCorriente.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbConductorPuestaTierra.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCanalizacionesCal.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbDesagues.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCanalizacionesAguaFria.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbSanitarios.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbTermos.currentText() != 'No hay actuaciones' or \
      self.ui.cmbCarpLigera.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbCarpMadera.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbRejas.currentText()!= 'No hay actuaciones' or \
      self.ui.cmbAscensores.currentText() != 'No hay actuaciones' or \
      self.ui.cmbEscalera.currentText() != 'No hay actuaciones' or \
      self.ui.cmbPortero.currentText() != 'No hay actuaciones' or \
      self.ui.cmbRampa.currentText() != 'No hay actuaciones'
     
  def getValues(self):
    return {'Pilotes': self.ui.cmbPilotes.currentText(),'PilotesAct' : self.ui.cmbPilotesAct.currentText(), \
            'Arquetas': self.ui.cmbArquetas.currentText(), 'ArquetasAct': self.ui.cmbArquetasAct.currentText(), \
            'Colectores': self.ui.cmbColectores.currentText(), 'ColectoresAct': self.ui.cmbColectoresAct.currentText(), \
            'Bajantes': self.ui.cmbBajantes.currentText(), 'BajantesAct': self.ui.cmbBajantesAct.currentText(), \
            'Forjados': self.ui.cmbForjados.currentText(), 'ForjadosAct': self.ui.cmbForjadosAct.currentText(), \
            'Fisuras': self.ui.cmbFisuras.currentText(), 'FisurasAct': self.ui.cmbFisurasAct.currentText(), \
            'Grietas': self.ui.cmbGrietas.currentText(), 'GrietasAct': self.ui.cmbGrietasAct.currentText(), \
            'LadFisuras': self.ui.cmbLadFisuras.currentText(), 'LadFisurasAct': self.ui.cmbLadFisurasAct.currentText(), \
            'LadGrietas': self.ui.cmbLadGrietas.currentText(), 'LadGrietasAct': self.ui.cmbLadGrietasAct.currentText(), \
            'LadHumSuelo': self.ui.cmbLadHumSuelo.currentText(), 'LadHumSueloAct': self.ui.cmbLadHumSueloAct.currentText(), \
            'LadHumTecho': self.ui.cmbLadHumTecho.currentText(), 'LadHumTechoAct': self.ui.cmbLadHumTechoAct.currentText(), \
            'IntFisuras': self.ui.cmbIntFisuras.currentText(), 'IntFisurasAct': self.ui.cmbIntFisurasAct.currentText(), \
            'IntGrietas': self.ui.cmbIntGrietas.currentText(), 'IntGrietasAct': self.ui.cmbIntGrietasAct.currentText(), \
            'HumSuelo': self.ui.cmbHumSuelo.currentText(), 'HumSueloAct': self.ui.cmbHumSueloAct.currentText(), \
            'CubHorCom': self.ui.cmbCubHorCom.currentText(), 'CubHorComAct': self.ui.cmbCubHorComAct.currentText(), \
            'CubHorFaldon': self.ui.cmbCubHorFaldon.currentText(), 'CubHorFaldonAct': self.ui.cmbCubHorFaldonAct.currentText(), \
            'CubHorEncParamVer': self.ui.cmbCubHorEncParamVer.currentText(), 'CubHorEncParamVerAct': self.ui.cmbCubHorEncParamVerAct.currentText(), \
            'CubHorEncCazoletas': self.ui.cmbCubHorEncCazoletas.currentText(), 'CubHorEncCazoletasAct': self.ui.cmbCubHorEncCazoletasAct.currentText(), \
            'CubIncCompleta': self.ui.cmbCubIncCompleta.currentText(), 'CubIncCompletaAct': self.ui.cmbCubIncCompletaAct.currentText(), \
            'CubIncFaldon': self.ui.cmbCubIncFaldon.currentText(), 'CubIncFaldonAct': self.ui.cmbCubIncFaldonAct.currentText(), \
            'CubIncRemates': self.ui.cmbCubIncRemates.currentText(), 'CubIncRematesAct': self.ui.cmbCubIncRematesAct.currentText(), \
            'CubIncEncParamVer': self.ui.cmbCubIncEncParamVer.currentText(), 'CubIncEncParamVerAct': self.ui.cmbCubIncEncParamVerAct.currentText(), \
            'Climatizacion': self.ui.cmbClimatizacion.currentText(), 'ClimatizacionAct': self.ui.cmbClimatizacionAct.currentText(), \
            'Radiadores': self.ui.cmbRadiadores.currentText(), 'RadiadoresAct': self.ui.cmbRadiadoresAct.currentText(), \
            'Circuitos': self.ui.cmbCircuitos.currentText(), 'CircuitosAct': self.ui.cmbCircuitosAct.currentText(), \
            'LineasYDerivaciones': self.ui.cmbLineasYDerivaciones.currentText(), 'LineasYDerivacionesAct': self.ui.cmbLineasYDerivacionesAct.currentText(), \
            'PuntosLuz': self.ui.cmbPuntosLuz.currentText(), 'PuntosLuzAct': self.ui.cmbPuntosLuzAct.currentText(), \
            'TomaCorriente': self.ui.cmbTomaCorriente.currentText(), 'TomaCorrienteAct': self.ui.cmbTomaCorrienteAct.currentText(), \
            'ConductorPuestaTierra': self.ui.cmbConductorPuestaTierra.currentText(), 'ConductorPuestaTierraAct': self.ui.cmbConductorPuestaTierraAct.currentText(), \
            'Canalizaciones': self.ui.cmbCanalizacionesCal.currentText(), 'CanalizacionesAct': self.ui.cmbCanalizacionesCalAct.currentText(), \
            'Desagues': self.ui.cmbDesagues.currentText(), 'DesaguesAct': self.ui.cmbDesaguesAct.currentText(), \
            'CanalizacionesAguaFria': self.ui.cmbCanalizacionesAguaFria.currentText(), 'CanalizacionesAguaFriaAct': self.ui.cmbCanalizacionesAguaFriaAct.currentText(), \
            'Sanitarios': self.ui.cmbSanitarios.currentText(), 'SanitariosAct': self.ui.cmbSanitariosAct.currentText(), \
            'Termos': self.ui.cmbTermos.currentText(), 'TermosAct': self.ui.cmbTermosAct.currentText(), \
            'CarpLigera': self.ui.cmbCarpLigera.currentText(), 'CarpLigeraAct': self.ui.cmbCarpLigeraAct.currentText(), \
            'CarpMadera': self.ui.cmbCarpMadera.currentText(), 'CarpMaderaAct': self.ui.cmbCarpMaderaAct.currentText(), \
            'Rejas': self.ui.cmbRejas.currentText(), 'RejasAct': self.ui.cmbRejasAct.currentText(), \
            'Ascensores': self.ui.cmbAscensores.currentText(), 'AscensoresAct': self.ui.spinAscensorAct.value(), \
            'Portero': self.ui.cmbPortero.currentText(), 'PorteroAct': self.ui.spinPorteroAct.value(),\
            'Escalera': self.ui.cmbEscalera.currentText(), 'EscaleraAct': self.plantas,\
            'Rampa': self.ui.cmbRampa.currentText(), 'RampaAct': self.ui.spinRampaAct.value()            
            }       