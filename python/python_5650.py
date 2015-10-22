# How to reference the same Model twice from another one?
class Translation(db.Model):
    origin = db.ReferenceProperty(Expression, required=True, collection_name='translation_origins')
    target = db.ReferenceProperty(Expression, required=True, collection_name='translation_targets')
