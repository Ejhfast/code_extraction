# Parsing dbpedia JSON in Python
print [abstract['value'] for abstract in json_data["http://dbpedia.org/resource/Ceramic_art"]["http://dbpedia.org/ontology/abstract"] if abstract['lang'] == 'en'][0]
