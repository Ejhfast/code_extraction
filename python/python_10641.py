# Overwrite import, show names of modules importing a module
import inspect
last_frame = inspect.stack()[1]
print 'Module imported from file:line_no = %s:%i' % last_frame[1:3]
