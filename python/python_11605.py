# MongoEngine ListField within a EmbeddedDocument throws TypeError on validation
class Features(EmbeddedDocument):
    version = FloatField()
    data = ListField(StringField())
