# encoding=utf8
import subprocess
import json
import os

class ConfigService:
    
    def getPath(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir,'config.txt')
        if os.path.exists(filename):
            try:
                with open(filename) as data_file:
                    data = json.load(data_file)
                    return unicode(data['path'])
            except:
                return dir
        else:
            return dir
    
    def savePath(self, path):
        data = {'path':path}        
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir,'config.txt')
        with open(filename, 'w+') as outfile:
            json.dump(data, outfile)
    
    def validatePath(self, path):
        try:
            print path
            return os.access(path, os.W_OK)
        except:
            return False      