# How to use python requests to PUT a pmml model to openscoring
r = requests.put('http://localhost:8080/openscoring/model/DecisionTreeIris', data=open(file, 'rb'), headers={'Content-type': 'text/xml', 'Accept': 'text/xml'})
