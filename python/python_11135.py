# Add a additional elements to service that are missing from WSDL in suds
obj = client.factory.create('ns1:object')
obj.newField = 'value'
