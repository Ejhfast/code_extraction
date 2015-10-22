# How to get path of a python module ( not sys.executable )
import MODULE, os
path = os.path.dirname(MODULE.__file__)
