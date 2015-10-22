# Filtering by the value of an internal list using MongoAlchemy
def groups(self):
    return Group.query.filter(
        {'participants': {'$elemMatch': {'participant_id': self.id}}}).all()
