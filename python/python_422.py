# How do I get all the entities of a type with a required property in Google App Engine?
class Jean(db.Model):
    sex = db.StringProperty(required=True, choices=set(["male", "female"]), default="male")
