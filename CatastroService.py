import requests
import httplib2
import xmltodict

class CatastroService:
    
    baseUrl = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"
    baseSoapAction = "http://tempuri.org/OVCServWeb/OVCCoordenadas/"
    defaultSRS = "EPSG:4326"
    
    consulta_RCOOR_Url = "/OVCCoordenadas.asmx/Consulta_RCCOOR"
    
    def getCoordsInfo(self, x, y):
        my_http_proxy = {'http':'http://127.0.0.1:8888'}
        params = { "Coordenada_X": x, "Coordenada_Y": y, "SRS": self.defaultSRS }   
        headers={'SOAPAction': self.baseSoapAction + 'Consulta_RCCOOR'}        
        url = self.baseUrl + self.consulta_RCOOR_Url
        
        response = requests.post(url, data=params, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        return responseDict['consulta_coordenadas']['coordenadas']['coord']    
                
    def getDireccion(self, x, y):  
        return self.getCoordsInfo(x,y)['ldt']               
    
    def getNumCatastro(self,x,y):
        pc = self.getCoordsInfo(x,y)['pc']
        return pc['pc1'] + pc['pc2']        