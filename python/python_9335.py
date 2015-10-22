# Programmatically disable "trap unhandled exceptions" mode in winpdb
import rpdb2; rpdb2.start_embedded_debugger('mypassword')
rpdb2.g_debugger.set_trap_unhandled_exceptions(False)
