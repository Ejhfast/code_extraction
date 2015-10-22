# Default Values for Models in Google App Engine
class Pet(db.Model):
    name = db.StringProperty(required=True, default="(unnamed)")
