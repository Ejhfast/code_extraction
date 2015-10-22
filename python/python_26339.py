# Peewee Model keyword can't be an expression on Update
q = Thunderdome.update(status='Updatedstatus')\
     .where(Thunderdome.port == '2310')
