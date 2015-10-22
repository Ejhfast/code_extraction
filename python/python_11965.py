# Ebay SOAP error with python suds
operation_name = {'X-EBAY-SOA-OPERATION-NAME':'findItemsByKeywords', 'SomeOther':'blabla'}
client = Client(EBAY_WSDL,headers=operation_name)
