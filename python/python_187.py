# Restarting a Python Interpreter Quietly
import savestate, pickle, __main__
pickle.dump(__main__, open('savestate.pickle', 'wb'), 2)
