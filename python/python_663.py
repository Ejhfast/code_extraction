# Recursive delete in google app engine
db.delete(Bottom.all(keys_only=True).filter("daddy =", top).fetch(1000))
