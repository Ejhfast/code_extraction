# How do you find out what python file calls a module function
import traceback
currentStack=traceback.extract_stack()
