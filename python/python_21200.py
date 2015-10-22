# How to check if Python3 was built with '--enable-shared'?
import sysconfig
sysconfig.get_config_vars('Py_ENABLE_SHARED')
