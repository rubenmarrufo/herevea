# encoding=utf8
import subprocess
import json
import os
from ConfigService import ConfigService
from Ui_ErrorDialog import Ui_ErrorDialog

class HuellaService:
	
	def Calculate(self, proyecto, usuario, actuaciones, demCons):
		try:
			configService = ConfigService()
			dir = configService.getPath()
			filename = os.path.join(dir,u'data.txt')
			proyecto.update(usuario)
			proyecto.update(actuaciones)
			proyecto.update(demCons)
			with open(filename, 'w+') as outfile:
				json.dump(proyecto, outfile)
			application = os.path.join(os.path.dirname(__file__),'toexcel/Herevea.exe')
			cmd = [application]
			process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
			process.wait()
			with open(os.path.join(dir,'result.txt')) as data_file:
				data = json.load(data_file)
			return data
		except:
			ui_Error = Ui_ErrorDialog(u'Hubo un error intentando realizar el análisis. Asegúrese de tener permisos de escritura sobre la carpeta de trabajo o seleccione una diferente en el menú Configuración')
			ui_Error.show()
			ui_Error.exec_()
			return None			
	
class InfoHuella:
	def __init__(self,proyecto,usuario,actuacion):
		self.proyecto=proyecto
		self.usuario=usuario
		self.actuacion=actuacion
		