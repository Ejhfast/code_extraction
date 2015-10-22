# Django: Getting path of module being imported from views.py
def getpath():
    os.path.abspath(os.path.dirname(__file__))
