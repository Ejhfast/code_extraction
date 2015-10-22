# SUDS SOAP "dependancies suds.TypeNotFound: Type not found" Error
from suds.client import Client
wsdl_url = 'http://46.51.221.138/PBExternalServices/v1/soap?wsdl'
client = Client(wsdl_url, autoblend=True)
