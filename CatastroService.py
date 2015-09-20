import requests
import httplib2
import xmltodict

class CatastroService:
    
    baseUrl = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"
    baseSoapAction = "http://tempuri.org/OVCServWeb"
    
    defaultSRS = "EPSG:4326"
    
    consulta_RCOOR_Url = "/OVCCoordenadas.asmx/Consulta_RCCOOR"
    consulta_DNPRC_Url = "/OVCCallejero.asmx/Consulta_DNPRC"
    consulta_Provincia_Url = "/OVCCallejero.asmx/ConsultaProvincia"
    consulta_Municipio_Url = "/OVCCallejero.asmx/ConsultaMunicipio"
                
    def getCoordsInfo(self, x, y):
        my_http_proxy = {'http':'http://127.0.0.1:8888'}
        params = { "Coordenada_X": x, "Coordenada_Y": y, "SRS": self.defaultSRS }   
        headers={'SOAPAction': self.baseSoapAction + '/OVCCoordenadas/Consulta_RCCOOR'}        
        url = self.baseUrl + self.consulta_RCOOR_Url
        
        response = requests.post(url, data=params, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        return responseDict['consulta_coordenadas']['coordenadas']['coord']
    
    def getParcelaInfo(self, numCatastro, provincia, municipio):
        my_http_proxy = {'http':'http://127.0.0.1:8888'}        
        params = { "Provincia": provincia, "Municipio": municipio, "RC": numCatastro }        
        headers={'SOAPAction': self.baseSoapAction + '/OVCCallejero/Consulta_DNPRC'}        
        url = self.baseUrl + self.consulta_DNPRC_Url
        
        response = requests.post(url, data=params, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        return responseDict['consulta_dnp']
    
    def getProvincias(self):
        my_http_proxy = {'http':'http://127.0.0.1:8888'}           
        headers={'SOAPAction': self.baseSoapAction + '/OVCCallejero/ConsultaProvincia'}        
        url = self.baseUrl + self.consulta_Provincia_Url
        
        response = requests.post(url, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        return responseDict['consulta_provinciero']['provinciero']['prov']

    def getMunicipios(self, provincia):
        my_http_proxy = {'http':'http://127.0.0.1:8888'} 
        params = { "Provincia": provincia, "Municipio":'' }          
        headers={'SOAPAction': self.baseSoapAction + '/OVCCallejero/ConsultaMunicipio'}        
        url = self.baseUrl + self.consulta_Municipio_Url
        
        response = requests.post(url, data=params, headers=headers)  
        responseDict = xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
        return responseDict['consulta_municipiero']['municipiero']['muni']
        
    def getDireccionesInmuebles(self, listInmueblesDic):
        listInmuebles = []
        for inmueble in listInmueblesDic:
            print(inmueble)
            print(listInmueblesDic)
            inmuebleRefCatDic = inmueble['rc']
            inmuebleRefCat = inmuebleRefCatDic['pc1'] + inmuebleRefCatDic['pc2'] + inmuebleRefCatDic['car']
            direccionExtDic = inmueble['dt']['locs']['lous']['lourb']['dir']
            direccionExt = direccionExtDic['tv'] + direccionExtDic['nv'] + direccionExtDic['pnp']
            direccionIntDic = inmueble['dt']['locs']['lous']['lourb']['loint']            
            inmuebleRow = [ inmuebleRefCat, direccionExt + direccionInt ]
            listInmuebles.append(inmuebleRow)
        return listInmuebles         
            