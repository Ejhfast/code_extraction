# How do I validate a JSON Schema schema, in Python?
from jsonschema import Draft3Validator
my_schema = json.loads(my_text_file) #or however else you end up with a dict of the schema
Draft3Validator.check_schema(schema)
