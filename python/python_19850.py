# IPython Step by step debugging of the imported module
from IPython.core.debugger import Pdb
ipdb = Pdb()
ipdb.runcall(my_imported_function, args...)
