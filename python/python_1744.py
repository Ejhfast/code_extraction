# mod_python not detecting files when using open()
import os.path
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardlist.xml'))
