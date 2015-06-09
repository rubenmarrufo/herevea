import requests
import httplib2
import xmltodict

class CatastroService:
    
    baseUrl = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"
    baseSoapAction = "http://tempuri.org/OVCServWeb/OVCCoordenadas/"
    defaultSRS = "EPSG:4326"
    
    consulta_RCOOR_Url = "/OVCCoordenadas.asmx/Consulta_RCCOOR"
                        
    def getInfo(self, x, y):  
        numCatastro = self.getNumCatastro(self, x, y)
        
        print numCatastro
    
    def getNumCatastro(self,x,y):
        my_http_proxy = {'http':'http://127.0.0.1:8888'}
        params = { "Coordenada_X": x, "Coordenada_Y": y, "SRS": self.defaultSRS }   
        headers={'SOAPAction': self.baseSoapAction + 'Consulta_RCCOOR'}        
        url = self.baseUrl + self.consulta_RCOOR_Url
        
        response = requests.post(url, data=params, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        numCatastroDict = responseDict['consulta_coordenadas']['coordenadas']['coord']['pc']
        numCatastro = numCatastroDict['pc1'] + numCatastroDict['pc2']