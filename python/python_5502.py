# SOAP suds and the dreaded schema Type Not Found error
imp = Import('http://schemas.xmlsoap.org/soap/encoding/', location='http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add('http://ws.client.com/Members.asmx')
client = Client(url,plugins=[ImportDoctor(imp)]
