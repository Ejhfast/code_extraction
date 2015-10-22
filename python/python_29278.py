# How can I detect if my python script/code was ran from a python unittest?
def hasRunFromUnitTest():
    return 'unittest' in sys.modules
