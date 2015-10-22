# Is there a way to detect the order of a module's globals() in python?
sys._getframe().f_code.co_names
