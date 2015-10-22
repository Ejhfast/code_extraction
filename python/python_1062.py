# Web Service client in Python using ZSI - "Classless struct didn't get dictionary"
from ZSI.ServiceProxy import ServiceProxy
service = ServiceProxy('test.wsdl')
service.NewOperation(NewOperationRequest='test')
