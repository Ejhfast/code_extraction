# How to turn these functions generic
@to_json
def getAllUsersFrom(db):
    return list(db.users.find())
