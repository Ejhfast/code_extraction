# SQLalchemy specify which index to use
session.query(Model).with_hint(Model, 'USE INDEX col1_index')
