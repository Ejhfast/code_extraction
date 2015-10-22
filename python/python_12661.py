# How to make custom array in python django
fields = [(d['FieldName'], d.get('FieldValue', '')) for d in your_list]
