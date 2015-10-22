# Elegantly suppress Twill output in Python
import os
f = open(os.devnull,"w")
twill.set_output(f)
