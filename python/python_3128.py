# Single-file storage for a Python application
ed_user = User('ed', 'Ed Jones', 'edspassword') #user is the class you mapped the table to
session.add(ed_user)
session.commit() # basically auto saving here :)
