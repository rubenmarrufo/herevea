# encoding=utf8
import subprocess
import json
import os

class HuellaService:
	
	def Calculate(self, proyecto, usuario, actuaciones, demCons):
		dir = os.path.dirname(__file__)
		filename = os.path.join(dir,'toexcel/data.txt')
		proyecto.update(usuario)
		proyecto.update(actuaciones)
		proyecto.update(demCons)
		with open(filename, 'w+') as outfile:
			json.dump(proyecto, outfile)
		application = os.path.join(dir,'toexcel/Herevea.exe')
		cmd = [application]
		process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
		process.wait()
		with open(os.path.join(dir,'toexcel/result.txt')) as data_file:
			data = json.load(data_file)
		return data
	
class InfoHuella:
	def __init__(self,proyecto,usuario,actuacion):
		self.proyecto=proyecto
		self.usuario=usuario
		self.actuacion=actuacion
		