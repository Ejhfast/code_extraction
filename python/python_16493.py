# how to pass collection name as variable in db.runCommand in mongodb
def func_(collection1):
    data = db.runCommand('aggregate', collection1, pipeline=pipe)
