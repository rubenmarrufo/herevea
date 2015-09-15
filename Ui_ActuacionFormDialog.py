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

class Ui_ActuacionFormDialog(QtGui.QDialog):
  def __init__(self, catastroService): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ActuacionForm()
    self.ui.setupUi(self)
    self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText('Calculo de huella')
    self.ui.tbxDireccion.setText(catastroService.getDireccion())
    self.ui.tbxRefCatastral.setText(catastroService.getNumCatastro())
    self.ui.tabWidget.setCurrentIndex(0)
    self.ui.pushButton.clicked.connect(self.backButton)    

  def backButton(self):
    self.back=True
    self.close()
      
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
            'HumTecho': self.ui.cmbHumTecho.currentText(), 'HumTechoAct': self.ui.cmbHumTechoAct.currentText(), \
            'CubHorCom': self.ui.cmbCubHorCom.currentText(), 'CubHorComAct': self.ui.cmbCubHorComAct.currentText(), \
            'CubHorFaldon': self.ui.cmbCubHorFaldon.currentText(), 'CubHorFaldonAct': self.ui.cmbCubHorFaldonAct.currentText(), \
            'CubHorEncParamVer': self.ui.cmbCubHorEncParamVer.currentText(), 'CubHorEncParamVerAct': self.ui.cmbCubHorEncParamVerAct.currentText(), \
            'CubHorEncCazoletas': self.ui.cmbCubHorEncCazoletas.currentText(), 'CubHorEncCazoletasAct': self.ui.cmbCubHorEncCazoletasAct.currentText(), \
            'CubIncCompleta': self.ui.cmbCubIncCompleta.currentText(), 'CubIncCompletaAct': self.ui.cmbCubIncCompletaAct.currentText(), \
            'CubIncFaldon': self.ui.cmbCubIncFaldon.currentText(), 'CubIncFaldonAct': self.ui.cmbCubIncFaldonAct.currentText(), \
            'CubIncRemates': self.ui.cmbCubIncRemates.currentText(), 'CubIncRematesAct': self.ui.cmbCubIncRematesAct.currentText(), \
            'CubIncEncParamVer': self.ui.cmbCubIncEncParamVer.currentText(), 'CubIncEncParamVerAct': self.ui.cmbCubIncEncParamVerAct.currentText(), \
            'Climatizacion': self.ui.cmbClimatizacion.currentText(), 'ClimatizacionAct': self.ui.cmbClimatizacionAct.currentText(), \
            'Conductos': self.ui.cmbConductos.currentText(), 'ConductosAct': self.ui.cmbConductosAct.currentText(), \
            'Radiadores': self.ui.cmbRadiadores.currentText(), 'RadiadoresAct': self.ui.cmbRadiadoresAct.currentText(), \
            'Circuitos': self.ui.cmbCircuitos.currentText(), 'CircuitosAct': self.ui.cmbCircuitosAct.currentText(), \
            'LineasYDerivaciones': self.ui.cmbLineasYDerivaciones.currentText(), 'LineasYDerivacionesAct': self.ui.cmbLineasYDerivacionesAct.currentText(), \
            'PuntosLuz': self.ui.cmbPuntosLuz.currentText(), 'PuntosLuzAct': self.ui.cmbPuntosLuzAct.currentText(), \
            'TomaCorriente': self.ui.cmbTomaCorriente.currentText(), 'TomaCorrienteAct': self.ui.cmbTomaCorrienteAct.currentText(), \
            'ConductorPuestaTierra': self.ui.cmbConductorPuestaTierra.currentText(), 'ConductorPuestaTierraAct': self.ui.cmbConductorPuestaTierraAct.currentText(), \
            'CanalizacionesCal': self.ui.cmbCanalizacionesCal.currentText(), 'CanalizacionesCalAct': self.ui.cmbCanalizacionesCalAct.currentText(), \
            'Desagues': self.ui.cmbDesagues.currentText(), 'DesaguesAct': self.ui.cmbDesaguesAct.currentText(), \
            'CanalizacionesAguaFria': self.ui.cmbCanalizacionesAguaFria.currentText(), 'CanalizacionesAguaFriaAct': self.ui.cmbCanalizacionesAguaFriaAct.currentText(), \
            'Griferia': self.ui.cmbGriferia.currentText(), 'GriferiaAct': self.ui.cmbGriferiaAct.currentText(), \
            'Sanitarios': self.ui.cmbSanitarios.currentText(), 'SanitariosAct': self.ui.cmbSanitariosAct.currentText(), \
            'Termos': self.ui.cmbTermos.currentText(), 'TermosAct': self.ui.cmbTermosAct.currentText(), \
            'Ascensores': self.ui.cmbAscensores.currentText(), 'AscensoresAct': self.ui.spbNumAscensores.value(), \
            'CarpLigera': self.ui.cmbCarpLigera.currentText(), 'CarpLigeraAct': self.ui.cmbCarpLigeraAct.currentText(), \
            'CarpMadera': self.ui.cmbCarpMadera.currentText(), 'CarpMaderaAct': self.ui.cmbCarpMaderaAct.currentText(), \
            'Rejas': self.ui.cmbRejas.currentText(), 'RejasAct': self.ui.cmbRejasAct.currentText()
            }       