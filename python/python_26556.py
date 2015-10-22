# How to handle and test Mongoengine objects with ReferenceField?
model = {'nome': 'nome', 'descricao': 'descricao',
          atividades: [str(ativ1['id']), str(ativ2['id'])]}
data = json.dumps(model)
