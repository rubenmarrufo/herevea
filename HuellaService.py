import subprocess
import json
import os

class HuellaService:
	
	def Calculate(self, actuaciones):
		dir = os.path.dirname(__file__)
		filename = os.path.join(dir,'toexcel/data.txt')
		with open(filename, 'w+') as outfile:
			json.dump(actuaciones, outfile)
		application = os.path.join(dir,'toexcel/Herevea.exe')
		cmd = [application]
		process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
		process.wait()
		with open(os.path.join(dir,'toexcel/result.txt')) as data_file:
			data = json.load(data_file)
		dummy=data
		return data