# function to print current module's name, also when called from another module
sys._getframe(1).f_globals.get('__name__', '__main__')
